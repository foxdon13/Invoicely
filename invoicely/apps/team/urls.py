from django.urls import path,include
from rest_framework import routers 
from .views import TeamViewSet

router = routers.DefaultRouter()
router.register("teams",TeamViewSet,basename='teams')

urlpatterns = [
    path('',include(router.urls))
]
