from django.urls import path , include
from . import  views
from rest_framework.routers import DefaultRouter

from .views import UserProfileViewSet, LoginViewSet

router = DefaultRouter()
router.register('profile', UserProfileViewSet, basename='profile')
router.register('login', LoginViewSet, basename='login')


urlpatterns = [
     path(r'', include(router.urls)),
]