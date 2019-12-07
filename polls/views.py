from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date') [:5]
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
    # The render() function takes the request object as ut first argument: request.
    # a template name as its second argument: 'polls/index.html'
    # a dictionary as its optional third argument: context
    # And it returns an HttpResponse object
    # return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

# A URLconf maps URL pattern to views

# def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # The get_object_or_404 function takes a Django model as its first element: Question
    # and and arbitrary number of keyword arguments wto the get() function of the model manager
    # it then raises an Http404 if the object doesn't exist
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question} )

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#     # response = "You're looking at the result of the vote of %s."
    # return HttpResponse(response % question_id)



# Remove old index, detail and results views and use Django's generic views

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by('pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary like object that lets you access submitted data by key name
        # the values returned are always string
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting for %s." %question_id)