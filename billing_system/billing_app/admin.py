from django.contrib import admin
from billing_app.models import  Bill
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Bill)
