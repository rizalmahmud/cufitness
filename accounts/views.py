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

# Import LangGraph's Graph class. Adjust the import based on your LangGraph installation.

from langgraph.graph import Graph



def easy_meal(request):
    return render(request, 'accounts/easy_meal.html')


def contact_trainer(request):
    return render(request, 'accounts/contact_trainer.html')


def healthy_meals(request):
    return render(request, 'accounts/healthy_meals.html')


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
    # For GET requests, show a confirmation page.
    return render(request, 'accounts/delete_account_confirm.html')


def workout_videos(request):
    # You can later pass context data if needed.
    return render(request, 'accounts/workout_videos.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@csrf_exempt  # For testing; ensure proper CSRF handling in production.
def chatbot_ai(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
        except Exception as e:
            return JsonResponse({'error': 'Invalid request body'}, status=400)

        # Check if the message is for a plan request
        if "diet plan" in user_message.lower() or "workout plan" in user_message.lower():
            # Define a system prompt tailored for plan requests.
            system_prompt = (
                "You are a helpful fitness assistant. "
                "When a user requests 'give me my diet plan' or 'give me my workout plan', "
                "respond with the appropriate plan. "
                "If the user asks for a diet plan, respond with details from the diet chart. "
                "If the user asks for a workout plan, respond with details from the workout chart."
            )

            # Define tool functions that return the appropriate plans.
            def get_diet_plan():
                return (
                    "Here is your Diet Plan:\n"
                    "• Breakfast: Oatmeal with berries\n"
                    "• Snack: Greek yogurt with honey\n"
                    "• Lunch: Grilled chicken salad\n"
                    "• Snack: Fruit (apple/orange)\n"
                    "• Dinner: Steamed fish, quinoa, and vegetables\n"
                    "Recommended Daily Calorie Intake: 2100 calories"
                )

            def get_workout_plan():
                return (
                    "Here is your Workout Plan:\n"
                    "• Cardio: 30 min run\n"
                    "• Weights: 3 sets x 10 reps (bench press, squats, etc.)\n"
                    "• Flexibility: 10 min stretching\n"
                    "• Balance: Core stability exercises"
                )

            # Map tool names to the functions.
            tools = {
                "get_diet_plan": get_diet_plan,
                "get_workout_plan": get_workout_plan,
            }

            # Create a LangGraph agent with the system prompt and tool mapping.
            agent_graph = Graph(system_prompt=system_prompt, tools=tools)

            # Prepare the message history for the agent.
            messages = [{"role": "user", "content": user_message}]

            # Invoke the agent graph to process the request.
            result = agent_graph.invoke({"messages": messages})

            # Extract the reply from the agent's response.
            reply = result.get("reply", "Sorry, I didn't understand that. Please try again.")
            return JsonResponse({"reply": reply})
        else:
            # Use the OpenAI Chat API for general fitness assistance.
            try:
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
            return JsonResponse({"reply": ai_message})
    return JsonResponse({"error": "Invalid request"}, status=400)


def ai_agent_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        user_message = data.get("message", "").strip()
        if not user_message:
            return JsonResponse({'reply': "Please provide a valid message."})

        # Define a system prompt (for reference purposes)
        system_prompt = (
            "You are a helpful fitness assistant. Based on the user's input, "
            "provide a personalized diet plan or workout plan. "
            "If the user says 'give me my diet plan', return a predefined diet plan. "
            "If they say 'give me my workout plan', return a predefined workout plan."
        )

        # Define tool functions that return plan details
        def get_diet_plan():
            return (
                "Hello Rizal, Welcome! \n\n"
                "Based on your height and weigh class I am giving you a specific diet plan.\n\n" 
                "Diet Plan for 2 kg Weight Loss:\n\n"
                "• Breakfast: Oatmeal with berries and a handful of almonds\n"
                "• Snack: Greek yogurt with honey\n"
                "• Lunch: Grilled chicken salad with mixed greens and vinaigrette\n"
                "• Snack: Fruit (apple or orange)\n"
                "• Dinner: Steamed fish, quinoa, and vegetables\n"
                "Recommended Daily Calorie Intake: 2100 calories"
            )

        def get_workout_plan():
            return (
                "Hello Rizal, Welcome!\n \n"
                
                 "Based on your height and weight class I am giving you a specific workout plan.\n \n"
                
                "Workout Plan:\n\n"
                "• Cardio: 30 min running\n"
                "• Weights: 3 sets x 10 reps (bench press, squats, etc.)\n"
                "• Flexibility: 10 min stretching\n"
                "• Balance: Core stability exercises"
            )

        # Simulate the AI agent logic with simple conditional checks:
        lower_msg = user_message.lower()
        if "diet plan" in lower_msg:
            reply_text = get_diet_plan()
        elif "workout plan" in lower_msg:
            reply_text = get_workout_plan()
        else:
            reply_text = "I'm sorry, I didn't understand that. Please ask for 'give me my diet plan' or 'give me my workout plan'."

        # Always return a JsonResponse
        return JsonResponse({'reply': reply_text})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)