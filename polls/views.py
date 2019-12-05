from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from django.http import Http404

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') [:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # The render() function takes the request object as ut first argument: request.
    # a template name as its second argument: 'polls/index.html'
    # a dictionary as its optional third argument: context
    # And it returns an HttpResponse object
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

# A URLconf maps URL pattern to views

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # The get_object_or_404 function takes a Django model as its first element: Question
    # and and arbitrary number of keyword arguments wto the get() function of the model manager
    # it then raises an Http404 if the object doesn't exist
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question} )

def results(request, question_id):
    response = "You're looking at the result of the vote of %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting for %s." %question_id)