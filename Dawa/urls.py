from django.urls import path, include
from.import views
from rest_framework.routers import DefaultRouter
from .views import DrugViewSet, OrderViewSet, PrescriptionViewSet, SupplierViewSet



router = DefaultRouter()
router.register('drugs', DrugViewSet)
router.register('orders', OrderViewSet)
router.register('prescriptions', PrescriptionViewSet)
router.register('suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
