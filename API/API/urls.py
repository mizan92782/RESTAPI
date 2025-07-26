"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from viewSetAPI.views import StudentViewSet

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'route', StudentViewSet, basename='student')

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    
    #other app urls
    path('function/',include('FunctionBasedAPI.urls')),
    path('class/',include('classBasedApi.urls')),
    path('mixin/',include('mixinApi.urls')),
    
    # vuewset api router
    path('',include(router.urls)),
    
    #! jwt login and refresh token
    # Token নেওয়ার জন্য
    path('class/all/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Token রিফ্রেশ করার জন্য
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]
