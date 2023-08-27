from django.shortcuts import render, redirect
from .models import Question
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@login_required(login_url="login")
def create_questions(request):
    user_id = request.session.get('user_id')
    if request.method == 'POST':
        question_text = request.POST.get('question', '')
        if question_text:
            question = Question(question=question_text, user=request.user)
            question.save()

    questions = Question.objects.filter(user=request.user)
    return render(request, "question.html", {'questions': questions})


@login_required(login_url="login")
def list_question(request):
    questions = Question.objects.all()
    return render(request, "list_question.html", {'questions': questions})


def construction_view(request):
    return render(request, "construction.html")
