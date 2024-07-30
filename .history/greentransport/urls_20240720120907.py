from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from greentransportapi.views.auth import check_user, register_user
from greentransportapi.views.user_view import UserView
from greentransportapi.views.scooter_view import ScooterView
from greentransportapi.views.maintenance_view import MaintenanceView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'scooters', ScooterView, 'scooter')
router.register(r'maintenance', MaintenanceView, 'maintenance')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
