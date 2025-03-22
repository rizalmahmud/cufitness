from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Goal
from .forms import GoalForm

@login_required
def my_goals(request):
    user = request.user
    goals = Goal.objects.filter(user=user)
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            new_goal = form.save(commit=False)
            new_goal.user = user
            new_goal.save()
            return redirect('my_goals')
    else:
        form = GoalForm()
    return render(request, 'goals/my_goals.html', {'goals': goals, 'form': form})
