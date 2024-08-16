from django.shortcuts import render
from .models import Question

# Create your views here.

def home_screen_view(request):
    
    context = {}
    
    questions = Question.objects.all()
    context['questions'] = questions
    

    return render(request, 'personal/home.html',context)