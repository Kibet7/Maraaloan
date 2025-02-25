# loan/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('apply/', views.apply_for_loan, name='apply_for_loan'),
    # path('status/', views.loan_status, name='loan_status'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('about/', views.about, name='about'),
    # path('verify-otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
    path('logout/', views.user_logout, name='logout'),
    path('contact/', views.contact, name='contact'),
     path('success/', views.success, name='success'),
    path('faq', views.faq, name='faq'),
    path('loans/', views.loans, name='loans'),
    path('investments/', views.investments, name='investments'),

]
