from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import CertificateViewSet

router = routers.DefaultRouter()
router.register(r'', CertificateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
