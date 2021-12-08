from django.urls import path, include
from rest_framework import routers
from .views import CertificateViewSet

router = routers.DefaultRouter()
router.register(r'',CertificateViewSet)
appname = 'certificates'

urlpatterns = [
    path('', include(router.urls)),


]