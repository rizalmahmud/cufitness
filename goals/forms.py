from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_text']
        widgets = {
            'goal_text': forms.TextInput(attrs={'placeholder': 'Enter your fitness goal (e.g., lose 5 kg, run 10 km)'}),
        }
