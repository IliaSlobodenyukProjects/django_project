from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from polls.models import Question


def index(request):
    polls = Question.objects.all()
    tt = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'polls': polls,
        'tt': tt
    }
    return HttpResponse(template.render(context, request))
