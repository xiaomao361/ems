"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls import url
from ems import views
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework_swagger.views import get_swagger_view
from rest_framework import routers
from ems import views
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'equipment', views.EquipmentViewSet, base_name='equipment')
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'groups', views.GroupViewSet, base_name='group')

schema_view = get_schema_view(title='open api', renderer_classes=[
    OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', schema_view, name='docs'),
    url(r'^index/', views.index),
    url(r'^login/', views.log_in),
    url(r'^logout/', views.logout),
    url(r'^index/', views.index),
    url(r'^equipment/', views.equipment),
    url(r'^detail/', views.detail),
    url(r'^result/', views.result),
    url(r'^$', views.index),
    url(r'^api/', include(router.urls)),
    # drf登录
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]