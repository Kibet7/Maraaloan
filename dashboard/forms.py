from django import forms
from .models import LoanApplicationss,LoanRepayment, EmployerAgreement
from .models import Profile


class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplicationss
        fields = ['full_name', 'email', 'phone', 'loan_amount', 'loan_duration', 'employment_status', 'id_number', 'kra_pin', 'id_scan', 'payslip',
                  'guarantor1_name', 'guarantor1_email', 'guarantor1_phone', 'guarantor1_employment_status', 'guarantor1_id_number', 'guarantor1_payslip',
                  'guarantor2_name', 'guarantor2_email', 'guarantor2_phone', 'guarantor2_employment_status', 'guarantor2_id_number', 'guarantor2_payslip']




class LoanRepaymentForm(forms.ModelForm):
    class Meta:
        model = LoanRepayment
        fields = ['name', 'amount', 'phone_number']  # Include the 'name' field
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
        }

class EmployerAgreementForm(forms.ModelForm):
    class Meta:
        model = EmployerAgreement
        fields = ['employer_name', 'employer_contact', 'agreement_file']
        widgets = {
            'employer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employer name'
            }),
            'employer_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Employer contact'
            }),
            'agreement_file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'phone_number', 'address', 'bio']
