"""greentransport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from greentransportapi.views.auth import check_user, register_user
from greentransportapi.views.scooters import ScooterView
from greentransportapi.views.maintenance import MaintenanceView
from greentransportapi.views.user_view import UserView
from greentransportapi.views.ride_view import RideView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'scooters', ScooterView, 'scooter')
router.register(r'maintenance', MaintenanceView, 'maintenance')
router.register(r'users', UserView, 'user')
router.register(r'rides', RideView, 'ride')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
