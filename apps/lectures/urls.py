from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import LectureViewSet

router = routers.DefaultRouter()
router.register(r'', LectureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
