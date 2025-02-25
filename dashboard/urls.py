from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('apply-now/', views.apply_now, name='apply_now'),

    path('status/', views.view_status, name='view_status'),
    path('repay_loan/', views.repay_loan, name='repay_loan'),
    path('submit-loan-application/', views.submit_loan_application, name='submit_loan_application'),
    path('bootstraplayout', views.bootstrap_layout, name='bootstraplayout'),
    path('application/', views.LoanApplicationss, name='application'),
    path('employer-agreement-success/', views.employer_aagreement_success, name='employer_aagreement_success'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('generate-employer-form/', views.generate_employer_form, name='generate_employer_form'),
    path('success/', views.loan_success, name='loan_success'),
]

