
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PlanViewSet
router = DefaultRouter()
router.register('plan', PlanViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
