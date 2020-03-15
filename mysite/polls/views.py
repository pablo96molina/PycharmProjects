from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from django.http import Http404
from django.views import generic

# Prueba de respuesta de votacion
#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "No seleccionaste una opción",
        })
    else:
        selected_choice.votes += 1
        selected_choice.Saldo += question.ValorMarket
        # Lo que hace esto es sumarle el valor del market a la columna de la respuesta, pero precisamos la forma de tener
        # un saldo que sea unico, probar una variable que se sume con ValorMarket o algo así
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    #Modelo generico sacado del tutorial de Django
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
