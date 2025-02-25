from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import LoanApplication, LoanPayment,ContactMessage,User

admin.site.register(LoanApplication)
admin.site.register(LoanPayment)
admin.site.register( ContactMessage)
admin.site.register(User)
