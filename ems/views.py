from django.shortcuts import render
from django.shortcuts import redirect
from ems import models
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib import admin
import logging

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
                logger.info('[Success] '+ username +' has logged in!')
                return redirect('/index/')
            else:
                message = "密码错误或未激活"
        else:
            message = "用户不存在！"
        logger.warning('[Failed] '+ username + ' failed to login!')
        return render(request, 'login.html', {"message": message})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')

@login_required
def index(request):
    pass
    return render(request, 'index.html', {'page': 'Dashboard'})

@login_required
def equipment(request):
    equs = models.Equipment.objects.all()
    return render(request, 'equipment.html', {'page': 'Equipment', 'equs': equs})

@login_required
def detail(request):
    if request.method == "GET":
         sn = request.GET['sn']
    # sn = request.POST['sn']
    # eqs = models.Equipment.objects.get(sn=sn)
    # return render(request, 'detail.html', {'page': 'detail', 'eqs': 'eqs'})
    return render(request, 'detail.html', {'page': sn})

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