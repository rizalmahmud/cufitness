from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, chatbot_ai, workout_videos, delete_account
from .views import healthy_meals
from .views import contact_trainer
from .views import easy_meal
from django.urls import path
from .views import ai_agent_view, register, profile, workout_videos, delete_account, chatbot_ai  # include your other views as needed




urlpatterns = [
    path('register/', register, name='register'),
    path('chatbot/', chatbot_ai, name='chatbot_ai'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', profile, name='profile'),
    path('workout_videos/', workout_videos, name='workout_videos'),
    path('delete_account/', delete_account, name='delete_account'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
path('healthy_meals/', healthy_meals, name='healthy_meals'),
path('contact_trainer/', contact_trainer, name='contact_trainer'),
path('easy_meal/', easy_meal, name='easy_meal'),
path('ai_agent/', ai_agent_view, name='ai_agent'),  # New URL for our AI agent view

]
