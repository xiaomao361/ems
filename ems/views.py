from django.shortcuts import render, redirect
import logging
import json
import crypt
import hashlib
import time
import os
import csv
from ems import models
from django.contrib.auth.decorators import login_required
from django.contrib import auth, admin
from django.contrib.auth import authenticate, login
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ems.serializer import EquipmentSerializer, UserSerializer, GroupSerializer
from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger('django')


# login for admin user
def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                logger.info('[Success] ' + username + ' has logged in!')
                return redirect('/index/')
            else:
                message = "用户未激活"
        else:
            message = "用户验证未通过"
        logger.warning('[Failed] ' + username + ' failed to login!')
        return render(request, 'login.html', {"message": message})
    else:
        return render(request, 'login.html')


# 登出
def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


# 首页
@login_required
def index(request):
    notices = models.Notice.objects.all()
    return render(request, 'index.html', {'page': 'Dashboard', 'notices': notices})

# 设备总览


@login_required
def equipment(request):
    equs = models.Equipment.objects.all()
    return render(request, 'equipment.html', {'page': 'Equipment', 'equs': equs})

# 结果展示页面


@login_required
def result(request):
    if request.method == "GET":
        condition = request.GET['condition']
        equs = models.Equipment.objects.filter(state=condition)
        return render(request, 'result.html', {'page': 'result', 'equs': equs})


# 设备详情页面


@login_required
def detail(request):
    if request.method == "GET":
        dict = {}
        i = 0
        sn = request.GET['sn']
        equ = models.Equipment.objects.get(sn=sn)
        merchant = models.Merchant.objects.get(name=equ.procurement)
        equ_historys = equ.history.all()

        for equ_history in equ_historys:
            date = equ_history.history_date
            user = equ_history.history_user_id
            type = equ_history.history_type
            if i == len(equ_historys)-1:
                dict[i] = {'date': date, 'user': user,
                           'type': type, 'changes': ''}
            else:
                new_record, old_record = equ_historys[i], equ_historys[i+1]
                delta = new_record.diff_against(old_record)
                dict[i] = {'date': date, 'user': user,
                           'type': type, 'changes': delta.changes}
            i += 1

        timelines = {}
        for value in dict.items():
            date = value[1].get('date').strftime('%Y-%m-%d')
            if timelines.get(date) == None:
                timelines[date] = []
            timelines.get(date).append(value)
        return render(request, 'detail.html',
                      {'page': 'detail',
                       'equ': equ,
                       'merchant': merchant,
                       'timelines': timelines})

# open api


@login_required
def apps(request):
    apps = models.OpenApp.objects.all()
    return render(request, 'apps.html', {'page': 'apps', 'apps': apps})


@login_required
def add_app(request):
    app_id = crypt.mksalt(crypt.METHOD_SHA512)
    app_key = hashlib.sha224(app_id.encode("utf-8")).hexdigest()
    models.OpenApp.objects.create(app_id=app_id, app_key=app_key)
    return redirect('/apps/')


@login_required
def del_app(request):
    app_id = request.GET['app_id']
    models.OpenApp.objects.get(app_id=app_id).delete()
    return redirect('/apps/')


@csrf_exempt
def get_equipment(request):
    if request.method == "POST":
        app_id = request.POST['app_id'].replace(' ', '')
        app_key = request.POST['app_key'].replace(' ', '')
        try:
            check_key = models.OpenApp.objects.get(app_id=app_id).app_key
        except models.OpenApp.DoesNotExist:
            check_key = None
        if app_key == check_key:
            equs = models.Equipment.objects.all()
            resp = {'code': 100, 'detail': serializers.serialize('json', equs)}
        else:
            resp = {'code': 403, 'detail': 'error app_id or app_key'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


class EquipmentViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a equipment instance.

    list:
        Return all equipment, ordered by most recently joined.

    create:
        Create a new equipment.

    delete:
        Remove an existing usequipmenter.

    partial_update:
        Update one or more fields on an existing equipment.

    update:
        Update a equipment.
    """

    queryset = models.Equipment.objects.all()
    serializer_class = EquipmentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# data


@login_required
def datas(request):
    datas = models.BakData.objects.all()
    return render(request, 'datas.html', {'page': 'datas', 'datas': datas})


@login_required
def add_data(request):
    now = time.strftime('%Y%m%d%H%M%S')
    os.system('python manage.py dumpdata --format=json > ./backup/' + now)
    size = os.path.getsize('./backup/' + now)
    models.BakData.objects.create(name=now, size=round(size/1024))
    return redirect('/datas/')


@login_required
def del_data(request):
    name = request.GET['name']
    models.BakData.objects.get(name=name).delete()
    os.system('rm -rf ./backup/' + name)
    return redirect('/datas/')


@login_required
def load_data(request):
    name = request.GET['name']
    os.system('python manage.py loaddata' + name)
    return redirect('/datas/')


@login_required
def download_data(request):
    name = request.GET['name']
    file = open('./backup/' + name, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="backup.json"'
    return response

# finicial


@login_required
def finicial(request):
    equs = models.Equipment.objects.all()
    return render(request, 'finicial.html', {'page': 'finicial', 'equs': equs})


def export_equs_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ems.csv"'
    writer = csv.writer(response)
    writer.writerow(['资产编号', '资产类别', '资产名称', 'SN码',
                     '状态', '使用人', '采购价格', '卖出价格', '备注'])
    equs = models.Equipment.objects.all().values_list('id', 'category', 'name', 'sn',
                                                      'state', 'user', 'price_in', 'price_out', 'remark')
    for equ in reversed(equs):
        writer.writerow(equ)
    return response

# lock


def lockscreen(request):
    user = request.user
    auth.logout(request)
    return render(request, 'lockscreen.html', {'page': 'lockscreen', 'user': user})

# notice


@login_required
def notices(request):
    notices = models.Notice.objects.all()
    return render(request, 'notices.html', {'page': 'notices', 'notices': notices})


@login_required
def notice(request):
    if request.method == "GET":
        id = request.GET['id']
        notice = models.Notice.objects.get(id=id)
        if notice.is_read == 0:
            notice.is_read = 1
            notice.save()
        return render(request, 'notice.html', {'page': 'notice', 'notice': notice})

def del_notice(request):
    if request.method == "GET":
        id = request.GET['id']
        notice = models.Notice.objects.get(id=id).delete()
        return redirect('/notices/')

def read_all_notices(request):
    models.Notice.objects.filter(is_read=0).update(is_read=1)
    return redirect('/index/')

# login for normal userg
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         message = "所有字段都必须填写！"
#         if username and password:
#             username = username.strip()
#             try:
#                 user = models.User.objects.get(name=username)
#                 if user.password == password:
#                     return redirect('/index/')
#                 else:
#                     message = "密码不正确！"
#             except:
#                 message = "用户名不存在！"
#         return render(request, 'login.html', {"message": message})
#     return render(request, 'login.html')
