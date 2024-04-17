# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('order-history', views.OrderHistoryView)

urlpatterns = [
    path('order-flower/', views.PlaceOrderView.as_view(), name='order'),
    path('', include(router.urls)),
]
