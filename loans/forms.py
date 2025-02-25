from django import forms
from django.contrib.auth.models import User
from .models import LoanApplication, ContactMessage

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     password_confirm = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email']

#     def clean_password_confirm(self):
#         password = self.cleaned_data.get('password')
#         password_confirm = self.cleaned_data.get('password_confirm')
#         if password != password_confirm:
#             raise forms.ValidationError("Passwords do not match!")
#         return password_confirm


from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    otp = forms.CharField(max_length=6, required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data






class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = LoanApplication
        fields = ['loan_amount', 'purpose']

    loan_amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Enter loan amount'}))
    purpose = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Purpose of loan'}))




class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
