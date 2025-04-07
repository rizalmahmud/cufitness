from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailUserCreationForm
import json
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'home.html')

def terms(request):
    return render(request, 'terms.html')

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Prepare confirmation email details
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
            # Send confirmation email
            send_mail(subject, message, from_email, recipient_list)
            # Log the user in and redirect to home page
            login(request, user)
            return redirect('home')
    else:
        form = EmailUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Your account has been permanently deleted.")
        return redirect('home')
    # For GET requests, show a confirmation page
    return render(request, 'accounts/delete_account_confirm.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@csrf_exempt  # For testing; handle CSRF properly in production
def chatbot_ai(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            openai.api_key = settings.OPENAI_API_KEY

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful fitness assistant."},
                    {"role": "user", "content": user_message},
                ],
                temperature=0.7,
            )
            ai_message = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            ai_message = "Sorry, I encountered an error processing your message."
        return JsonResponse({'reply': ai_message})
    return JsonResponse({'error': 'Invalid request'}, status=400)
