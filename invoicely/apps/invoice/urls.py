from django.urls import path,include
from rest_framework import routers, urlpatterns
from .views import InvoiceViewSet,ItemViewSet

router = routers.DefaultRouter()
router.register("invoices",InvoiceViewSet,basename='invoices')
router.register("items",ItemViewSet,basename='items')
urlpatterns= [
    path("",include(router.urls)),
]