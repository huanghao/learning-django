import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

from polls.models import Poll


# Create your views here.


def hello(request):
    return render(request, "hello.html")


def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse('<html><body>It is now %s.</body></html>' % now)


def hours_ahead(request, offset):
    offset = int(offset)
    now = datetime.datetime.now() 
    dt = now + datetime.timedelta(hours=offset)
    return render(request, "datetime.html", {
            'now': now,
            'offset': offset,
            'dt': dt,
            })






def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))


def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    # Uncomment this
    # poll = get_object_or_404(Poll, pk=poll_id)

    return render(request, 'polls/detail.html', {'poll': poll})



def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

