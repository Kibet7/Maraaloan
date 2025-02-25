from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LoanApplicationss(models.Model):
    # Borrower Details
    full_name = models.CharField(max_length=255)
    email = models.EmailField(default='example@example.com')  # Default email if not provided
    phone = models.CharField(max_length=15)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_duration = models.IntegerField()
    employment_status = models.CharField(
        max_length=50,
        choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')],
        default='Employed'  # Default to 'Employed' if not selected
    )
    id_number = models.CharField(max_length=20)
    kra_pin = models.CharField(max_length=20, blank=True, null=True)  # Optional field
    id_scan = models.FileField(upload_to='id_scans/', blank=True, null=True)  # Optional field
    payslip = models.FileField(upload_to='payslips/', blank=True, null=True)  # Optional field

    # Guarantor 1 Details (Optional)
    guarantor1_name = models.CharField(max_length=255, blank=True, null=True)
    guarantor1_email = models.EmailField(blank=True, null=True)
    guarantor1_phone = models.CharField(max_length=15, blank=True, null=True)
    guarantor1_employment_status = models.CharField(
        max_length=50,
        choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')],
        default='Employed',  # Default to 'Employed' if not selected
        blank=True, null=True
    )
    guarantor1_id_number = models.CharField(max_length=20, blank=True, null=True)
    guarantor1_payslip = models.FileField(upload_to='guarantor1_payslips/', blank=True, null=True)

    # Guarantor 2 Details (Optional)
    guarantor2_name = models.CharField(max_length=255, blank=True, null=True)
    guarantor2_email = models.EmailField(blank=True, null=True)
    guarantor2_phone = models.CharField(max_length=15, blank=True, null=True)
    guarantor2_employment_status = models.CharField(
        max_length=50,
        choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')],
        default='Employed',  # Default to 'Employed' if not selected
        blank=True, null=True
    )
    guarantor2_id_number = models.CharField(max_length=20, blank=True, null=True)
    guarantor2_payslip = models.FileField(upload_to='guarantor2_payslips/', blank=True, null=True)

    def __str__(self):
        return f"Loan Application for {self.full_name}"


#
# class LoanApplication(models.Model):
#     # Borrower Details
#     full_name = models.CharField(max_length=255, null=True)
#     email = models.EmailField(null=True)
#     phone = models.CharField(max_length=15)
#     loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
#     loan_duration = models.IntegerField()  # Duration in months
#     employment_status = models.CharField(max_length=20, null=True, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')])
#     id_number = models.CharField(max_length=20)
#     kra_pin = models.CharField(max_length=20)
#     id_scan = models.FileField(upload_to='uploads/ids/')
#     payslip = models.FileField(upload_to='uploads/payslips/')
#
#     # Guarantor 1 Details
#     guarantor1_name = models.CharField(max_length=255,null=True)
#     guarantor1_email = models.EmailField(null=True)
#     guarantor1_phone = models.CharField(max_length=15)
#     guarantor1_employment_status = models.CharField(max_length=20,null=True, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')])
#     guarantor1_id_number = models.CharField(max_length=20,null=True)
#     guarantor1_payslip = models.FileField(upload_to='uploads/guarantors/payslips/')
#
#     # Guarantor 2 Details
#     guarantor2_name = models.CharField(max_length=255,null=True,)
#     guarantor2_email = models.EmailField(null=True)
#     guarantor2_phone = models.CharField(max_length=15)
#     guarantor2_employment_status = models.CharField(max_length=20,null=True, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')])
#     guarantor2_id_number = models.CharField(max_length=20,null=True)
#     guarantor2_payslip = models.FileField(upload_to='uploads/guarantors/payslips/')
#
#     def __str__(self):
#         return self.full_name



class LoanRepayment(models.Model):
    borrower = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Loan Repayment"
        verbose_name_plural = "Loan Repayments"


class EmployerAgreement(models.Model):
    borrower = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    employer_name = models.CharField(max_length=255)
    employer_contact = models.CharField(max_length=15)
    agreement_file = models.FileField(upload_to='agreements/')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Employer Agreement"
        verbose_name_plural = "Employer Agreements"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    repayment_period = models.IntegerField()  # In months
    status = models.CharField(max_length=20, default="Pending")
    applied_date = models.DateField(auto_now_add=True)

    from django.db import models
class Testimonial(models.Model):
        name = models.CharField(max_length=100)  # Name of the user
        comment = models.TextField()  # The testimonial comment
        image = models.ImageField(upload_to='testimonials/', null=True, blank=True)  # Image uploaded via admin

        def __str__(self):
            return f"{self.name} - {self.comment[:50]}..."  # Display a short preview of the comment
