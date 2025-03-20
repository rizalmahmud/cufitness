from django.urls import path
from . import views

urlpatterns = [
    # Main My Workouts page
    path('', views.my_workouts, name='my_workouts'),
    # Specific workout routines
    path('cardio/', views.cardio, name='cardio'),
    path('weights/', views.weights, name='weights'),
    path('flexibility/', views.flexibility, name='flexibility'),
    path('balance/', views.balance, name='balance'),

]
