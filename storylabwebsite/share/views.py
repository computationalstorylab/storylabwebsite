from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import Paper


def index(request):
    latest_paper_list = Paper.objects.order_by('-pub_date')[:5]
    context = {'latest_paper_list': latest_paper_list}
    return render(request, 'share/index.html', context)