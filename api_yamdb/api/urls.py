from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TitleViewSet

router = DefaultRouter()
router.register('title', TitleViewSet)
urlpatterns = [
    path('v1/', include(router.urls)),
]
