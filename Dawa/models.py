

# Create your models here.
from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drug(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Prescription(models.Model):
    client_name = models.CharField(max_length=100)
    prescription_note = models.TextField()
    uploaded_file = models.FileField(upload_to='prescriptions/', null=True, blank=True)
    date = models.DateField(auto_now_add=True)

class Order(models.Model):
    client_name = models.CharField(max_length=100)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True)
