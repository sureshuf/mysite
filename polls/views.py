from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404

def index(request):
    latest_question_list = "Suresh"
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
