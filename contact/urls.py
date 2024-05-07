from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactusViewset

router = DefaultRouter()
router.register('', ContactusViewset)

urlpatterns = [
    path('', include(router.urls)),
]
