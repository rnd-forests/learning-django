from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     # The context is a dictionary mapping template variable
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))
#     # We can use a shortcut here --> better
#     # return render(request, 'polls/index.html', context)

# Use generic view
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")

#     # Better way to find a record or throw an exception
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
class DetailView(generic.DetailView):
    # generic.DetailView view expects the primary key value captured from the URL
    # to be 'pk'. As a result, we've to change the URL pattern from 'quesiton_id' to 'pk'
    model = Question
    template_name = 'polls/detail.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object containing submitted data.
        # Here the ID of the selected choice is returned as a string
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # If the choice ID doesn't exits in request data or
        # we cannot find the given choice, we redisplay the question form
        # together with an error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        # Increment votes for a choice
        selected_choice.votes += 1
        selected_choice.save()

        # Return a redirect response
        # We use reverse() function to prevent having to hardcode a URL in the view function
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    return HttpResponse("You're voting on question %s." % question_id)
