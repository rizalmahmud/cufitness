from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, chatbot_ai, workout_videos, delete_account
from .views import healthy_meals
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', register, name='register'),
    path('chatbot/', chatbot_ai, name='chatbot_ai'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('workout_videos/', workout_videos, name='workout_videos'),
    path('delete_account/', delete_account, name='delete_account'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
path('healthy_meals/', healthy_meals, name='healthy_meals'),
path('contact_trainer/', views.contact_trainer, name='contact_trainer'),  # Personal trainer by Rizal

]
