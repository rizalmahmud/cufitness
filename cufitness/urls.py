
from django.contrib import admin
from django.urls import path, include
from accounts.views import home  # Import the home view from accounts
from django.contrib.auth import views as auth_views
from accounts.views import home, terms


urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include URLs from the accounts app
path('password-reset/',
     auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
     name='password_reset'),
path('password-reset/done/',
     auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
     name='password_reset_confirm'),
path('password-reset-complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
path('workouts/', include('workouts.urls')),
path('terms/', terms, name='terms'),
 path('goals/', include('goals.urls')),  # new URL for goals

]
