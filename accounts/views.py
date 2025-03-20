from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmailUserCreationForm

def home(request):
    return render(request, 'home.html')
def terms(request):
    return render(request, 'terms.html')

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')
    else:
        form = EmailUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
from django.shortcuts import render

def profile(request):
    return render(request, 'accounts/profile.html')
