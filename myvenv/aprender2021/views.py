from django.shortcuts import render

from django.http import HttpResponse

from .models import Question,Choice

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'aprender2021/index.html', context)

def votes(request):
    votes = Choice.objects.all()
    context = {
        'votes': votes
    }
    return render(request, 'aprender2021/votes.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
