from django.shortcuts import render
from django.shortcuts import redirect
from ems import models
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib import admin
import logging
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from ems.serializer import EquipmentSerializer, UserSerializer, GroupSerializer
from datetime import datetime

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
                message = "密码错误或未激活"
        else:
            message = "用户不存在！"
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

# login for normal user
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
