from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'loans/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'loans/register.html')

        # Use create_user to save user with hashed password
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'loans/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate using Django's built-in method
        user = authenticate(request, username=username, password=password)  # username=email if you use email as the username
        if user is not None:
            login(request, user)  # Log the user in and start the session
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('dashboard')  # Redirect to the dashboard or appropriate page
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'registration/login.html')

    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'loans/home.html')

def about(request):
    return render(request, 'loans/about.html')


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout






def contact(request):
    if request.method == 'POST':
        # If the form is submitted, validate and save the data
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            # Optionally, you can display a success message
            return redirect('success')  # Redirect after successful submission
        else:
            return render(request, 'loans/contact.html', {'form': form, 'error': 'There was an error submitting the form.'})
    else:
        # GET request, just display the form
        form = ContactForm()
        return render(request, 'loans/contact.html', {'form': form})
    
    # views.py
def success(request):
    return render(request, 'loans/contactsucess.html', {'message': 'Your message has been sent successfully.'})

def faq(request):
    return render(request, 'loans/faq.html')


def loans(request):
    return render(request, 'loans/loans.html')

def investments(request):
    return render(request, 'loans/investments.html')