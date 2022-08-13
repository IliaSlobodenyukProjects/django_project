from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class PollsListView(generic.ListView):
    template_name = 'polls/polls_list.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class PollDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/poll_detail.html'


class PollResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/poll_results.html'


def vote(request, question_id):
    # same as above, no changes needed.
    pass
