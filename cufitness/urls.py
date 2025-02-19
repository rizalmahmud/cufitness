from django.contrib import admin
from django.urls import path, include
from accounts.views import home  # Import the home view from accounts

urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include URLs from the accounts app
]
