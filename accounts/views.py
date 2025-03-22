from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmailUserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Delete the user and log them out automatically
        user = request.user
        user.delete()
        messages.success(request, "Your account has been permanently deleted.")
        return redirect('home')
    # For GET request, show the confirmation page
    return render(request, 'accounts/delete_account_confirm.html')


def home(request):
    return render(request, 'home.html')
def terms(request):
    return render(request, 'terms.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Prepare email details
            subject = "Welcome to CUFitness"
            message = (
                f"Hi {user.username},\n\n"
                "Thank you for registering at CUFitness! Your registration is successful.\n"
                "We're excited to have you on board and look forward to helping you achieve your fitness goals.\n\n"
                "Best regards,\n"
                "The CUFitness Team"
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]

            # Send the confirmation email
            send_mail(subject, message, from_email, recipient_list)

            # Log the user in and redirect
            login(request, user)
            return redirect('home')
    else:
        form = EmailUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


from django.shortcuts import render

def profile(request):
    return render(request, 'accounts/profile.html')
