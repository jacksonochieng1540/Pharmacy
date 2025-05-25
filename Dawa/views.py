from django.shortcuts import render
from rest_framework import viewsets
from .models import Drug, Order, Prescription, Supplier
from .serializers import DrugSerializer, OrderSerializer, PrescriptionSerializer, SupplierSerializer

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


def home(request):
    return render(request,'home.html')

# Create your views here.
