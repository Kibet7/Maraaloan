from django.contrib import admin
from .models import Profile,LoanApplicationss,EmployerAgreement,Loan,LoanRepayment,Testimonial

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'address']

admin.site.register(LoanApplicationss)
admin.site.register(EmployerAgreement)
admin.site.register(Loan)
admin.site.register(LoanRepayment)
admin.site.register(Testimonial)
