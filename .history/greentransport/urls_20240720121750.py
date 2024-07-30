from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from greentransportapi.views.auth import check_user, register_user
from greentransportapi.views.user_view import UserView
from greentransportapi.views.scooters import ScooterView
from greentransportapi.views.ride_view import RideView
from greentransportapi.views.maintenance import MaintenanceView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'scooters', ScooterView, 'scooter')
router.register(r'maintenance', MaintenanceView, 'maintenance')
router.register(r'users', UserView, 'user')
router.register(r'rides', RideView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
