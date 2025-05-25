from django.contrib import admin

# Register your models here.
from .models import Drug, Order, Prescription, Supplier
admin.site.register(Drug),
admin.site.register(Order),
admin.site.register(Prescription),
admin.site.register(Supplier),