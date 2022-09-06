from django.http import HttpResponse
from .models import Question
from django.template import loader

from django.shortcuts import render

# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))