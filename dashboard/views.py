from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import ProfileForm,LoanApplicationss
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from .models import Loan
import requests
from django.shortcuts import render, redirect
from .forms import LoanApplicationForm,LoanRepaymentForm, EmployerAgreementForm
from django.contrib import messages




# Create your views here.


@login_required()
def dashboard(request):
    return render(request,'dashboard/dashboard.html')


def apply_now(request):
    return render(request,'dashboard/apply_now.html')

def FAQ(request):
    return render(request,'dashboard/faq.html')



@login_required
def view_status(request):
    # Mock data for demonstration purposes
    loan_status = {
        "status": "Pending",  # Options: "Verified", "Pending", "Rejected"
        "stage": "Document Verification",  # Stage the loan is currently in
        "remarks": "Please upload the required documents to proceed."
    }

    return render(request, 'dashboard/view_status.html', {"loan_status": loan_status})


def bootstrap_layout(request):
    return render(request, 'dashboard/bootstraplayout.html')


@csrf_exempt
def apply_for_loan(request):
    if request.method == 'POST':
        # Handle form submission
        form = LoanApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the loan application data to the database
            loan_application = form.save()

            # Redirect to a success page after saving
            return redirect('loan_success')
        else:
            return render(request, 'dashboard/apply_now.html', {'form': form})
    else:
        # Display the empty form
        form = LoanApplicationForm()
        return render(request, 'dashboard/apply_now.html', {'form': form})

def loan_success(request):
    # Display a success message or page after the loan is successfully applied
    return render(request, 'dashboard/loan_success.html')


@login_required
def submit_loan_application(request):
    if request.method == 'POST':
        # Collect form data
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        loan_amount = request.POST.get('loan_amount', 0)
        loan_duration = request.POST.get('loan_duration', 0)
        employment_status = request.POST.get('employment_status', 'Employed')
        id_number = request.POST.get('id_number', '')
        kra_pin = request.POST.get('kra_pin', '')

        # Handle file uploads
        id_scan = request.FILES.get('id_scan')
        payslip = request.FILES.get('payslip')

        # Guarantor 1 details
        guarantor1_name = request.POST.get('guarantor1_name', '')
        guarantor1_email = request.POST.get('guarantor1_email', '')
        guarantor1_phone = request.POST.get('guarantor1_phone', '')
        guarantor1_employment_status = request.POST.get('guarantor1_employment_status', 'Employed')
        guarantor1_id_number = request.POST.get('guarantor1_id_number', '')
        guarantor1_payslip = request.FILES.get('guarantor1_payslip')

        # Guarantor 2 details
        guarantor2_name = request.POST.get('guarantor2_name', '')
        guarantor2_email = request.POST.get('guarantor2_email', '')
        guarantor2_phone = request.POST.get('guarantor2_phone', '')
        guarantor2_employment_status = request.POST.get('guarantor2_employment_status', 'Employed')
        guarantor2_id_number = request.POST.get('guarantor2_id_number', '')
        guarantor2_payslip = request.FILES.get('guarantor2_payslip')

        # Save to the database
        loan_application = LoanApplicationss(
            full_name=full_name,
            email=email,
            phone=phone,
            loan_amount=loan_amount,
            loan_duration=loan_duration,
            employment_status=employment_status,
            id_number=id_number,
            kra_pin=kra_pin,
            id_scan=id_scan,
            payslip=payslip,
            guarantor1_name=guarantor1_name,
            guarantor1_email=guarantor1_email,
            guarantor1_phone=guarantor1_phone,
            guarantor1_employment_status=guarantor1_employment_status,
            guarantor1_id_number=guarantor1_id_number,
            guarantor1_payslip=guarantor1_payslip,
            guarantor2_name=guarantor2_name,
            guarantor2_email=guarantor2_email,
            guarantor2_phone=guarantor2_phone,
            guarantor2_employment_status=guarantor2_employment_status,
            guarantor2_id_number=guarantor2_id_number,
            guarantor2_payslip=guarantor2_payslip
        )
        loan_application.save()

        messages.success(request, "Your loan application has been submitted successfully!")
        return redirect('apply_now')  # Ensure 'apply_now' is correctly mapped in urls.py

    return render(request, 'dashboard/apply_now.html')


def repay_loan(request):
    repayment_form = LoanRepaymentForm()
    employer_form = EmployerAgreementForm()
    error = None

    if request.method == 'POST':
        if 'amount' in request.POST:  # Loan repayment form
            repayment_form = LoanRepaymentForm(request.POST)
            if repayment_form.is_valid():
                repayment = repayment_form.save(commit=False)
                repayment.borrower = request.user
                repayment.save()
                # M-Pesa API Call
                response = mpesa_payment(repayment.phone_number, repayment.amount)
                if response['ResponseCode'] == '0':
                    return redirect('success_page')
                else:
                    error = response.get('errorMessage', 'Payment failed. Try again.')
        elif 'employer_name' in request.POST:  # Employer agreement form
            employer_form = EmployerAgreementForm(request.POST, request.FILES)
            if employer_form.is_valid():
                agreement = employer_form.save(commit=False)
                agreement.borrower = request.user
                agreement.save()
                return redirect('employer_aagreement_success')  # Replace with your success redirect

    return render(request, 'dashboard/repay_loan.html', {
        'repayment_form': repayment_form,
        'employer_form': employer_form,
        'error': error
    })

def mpesa_payment(phone_number, amount):

    consumer_key = '2bgxUKmGSEAVwTQy3P67WFfbL8DIsKEKGN0XubepuzEs0zuX'
    consumer_secret = 'w7MxbfwQT81jbO6HMySpTkJRuQTULNgu1GbfzAmp5qTy6BoU4Mr2CQ1gGoG9ezvU'
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    # Obtain access token
    auth_response = requests.get(access_token_url, auth=(consumer_key, consumer_secret))
    access_token = auth_response.json().get('access_token')

    payment_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {'Authorization': f'Bearer {access_token}'}
    payload = {
        "BusinessShortCode": "174379",
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTYwMjE2MTY1NjI3",
        "Timestamp": "20160216165627",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "amount",
        "PartyA": "phone_number",
        "PartyB": "174379",
        "PhoneNumber": "254708374149",
        "CallBackURL": "https://mydomain.com/pat",
        "AccountReference": "Test",
        "TransactionDesc": "Test"
    }
    response = requests.post(payment_url, json=payload, headers=headers)
    return response.json()


@login_required
def view_status(request):    
    loan = LoanApplicationss.objects.filter(email=request.user.email).last()
    
    if loan:
        loan_status = {
            "status": "Approved",  # Example status; change as needed
            "stage": "Final Approval",
            "remarks": (
                "Congratulations! Your loan application is a success. "
                "Due to many applications and many unsuccessful requests, the company policy requires the applicant to pay a processing fee of "
                "<strong>250</strong>, which is included when the applicant receives the loan. The payment is exactly <strong>250</strong> and should be paid to the following till number."
            ),
            "show_till": True  # Show the payment till number section
        }
    else:
        loan_status = {
            "status": "No Application",
            "stage": "N/A",
            "remarks": "You haven't applied for any loan yet. Please apply to check your status.",
            "show_till": False  # Hide the payment till number section
        }

    return render(request, 'loan_status.html', {'loan_status': loan_status})


def employer_aagreement_success(request):
    return render(request, 'dashboard/employer_aagreement_success.html')


@login_required
def profile(request):
    return render(request, 'dashboard/profile.html', {'user': request.user})

def edit_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'dashboard/edit_profile.html', {'form': form})


def employer_form(request):
    return render(request,'dashboard/employer_agreement_form.html')


@login_required
def generate_employer_form(request):
    user = request.user
    loan = Loan.objects.filter(user=user).last()

    if not loan:
        return HttpResponse("No loan application found for the user.", status=404)

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Employer_Agreement_Form.pdf"'

    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle("Employer Agreement Form")

    # Rusonik Loans Details
    rusonik_info = (
        "Rusonik Loans\n"
        "P.O. Box 12345-00100, Nairobi, Kenya\n"
        "Email: info@rusonikloans.com | Phone: +254 712 345 678\n"
        "KCB Account: 123456789 | Equity Account: 987654321\n"
        "Paybill: 123456 (Account Name: Rusonik Loans)\n"
    )

    # PDF content
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(1 * inch, 10.5 * inch, "Employer Agreement Form")

    # Draw Rusonik Loan Details
    text = pdf.beginText(1 * inch, 10.0 * inch)
    text.setFont("Helvetica", 10)
    for line in rusonik_info.split("\n"):
        text.textLine(line)
    pdf.drawText(text)

    # Borrower details
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(1 * inch, 9.0 * inch, "Borrower Details:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(1 * inch, 8.7 * inch, f"Name: {user.first_name} {user.last_name}")
    pdf.drawString(1 * inch, 8.4 * inch, f"National ID: {user.profile.national_id}")
    pdf.drawString(1 * inch, 8.1 * inch, f"Loan Amount: KES {loan.amount:,}")
    pdf.drawString(1 * inch, 7.8 * inch, f"Repayment Period: {loan.repayment_period} months")

    # Employer details
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(1 * inch, 7.3 * inch, "Employer Details:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(1 * inch, 6.9 * inch, "Employer Name: _____________________________")
    pdf.drawString(1 * inch, 6.6 * inch, "Employee Status (e.g., Permanent/Contract): _____________________________")
    pdf.drawString(1 * inch, 6.3 * inch, "Trustworthiness of Employee: _____________________________")
    pdf.drawString(1 * inch, 6.0 * inch, "Intended Period of Employment: _____________________________")

    # Payment details
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(1 * inch, 5.5 * inch, "Payment Details:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(1 * inch, 5.1 * inch, "KCB Account: 123456789")
    pdf.drawString(1 * inch, 4.8 * inch, "Equity Account: 987654321")
    pdf.drawString(1 * inch, 4.5 * inch, "Paybill: 123456 (Rusonik Loans)")

    # Authorization
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(1 * inch, 4.0 * inch, "Authorization:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(1 * inch, 3.7 * inch, "We authorize the deduction of loan repayments from the employee's salary.")

    # Signatures
    pdf.drawString(1 * inch, 3.2 * inch, "HR Manager Signature: _____________________________")
    pdf.drawString(1 * inch, 2.8 * inch, "Accounts Officer Signature: _____________________________")
    pdf.drawString(1 * inch, 2.4 * inch, "Employer Stamp: _____________________________")
    pdf.drawString(1 * inch, 2.0 * inch, "Borrower Signature: _____________________________")

    pdf.save()
    return response


from .models import Testimonial

def dashboard(request):
    # Fetch all testimonials from the database
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials
    }

    return render(request, 'dashboard/dashboard.html', context)