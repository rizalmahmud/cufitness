from django.shortcuts import render

# Existing view for the "My Workouts" page
def my_workouts(request):
    return render(request, 'workouts/my_workouts.html')

# New views for each workout routine
def cardio(request):
    return render(request, 'workouts/cardio.html')

def weights(request):
    return render(request, 'workouts/weights.html')

def flexibility(request):
    return render(request, 'workouts/flexibility.html')

def balance(request):
    return render(request, 'workouts/balance.html')
