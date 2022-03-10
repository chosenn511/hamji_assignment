import requests
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from rest_framework import viewsets

from utils.url import restify

from .models import Choice, Question
from .serializers import QuestionSerializer


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        response = requests.get(restify("/questions/"))
        questions = response.json()

        # TODO#2 Show questions that are not yet closed
        open_questions = []
        for question in questions:
            if question["close_date"] is None:
                open_questions.append(question)
        open_questions.sort(key=lambda x: x["pub_date"], reverse=True)
        return open_questions[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    # TODO#1 Raise 404 if no matching question
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        queryset = self.get_queryset()
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get(pk=pk)
        except queryset.model.DoesNotExist:
            raise Http404("No such question exists.")
        return obj


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# API
# ===


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
