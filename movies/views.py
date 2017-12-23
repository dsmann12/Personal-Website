# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Review

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'review_list'
    #paginate_by = 5

    # prevents posts with a pub_date in future from showing
    def get_queryset(self):
        return Review.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Review
    template_name = 'movies/detail.html'

    # exclude posts that aren't published yet
    def get_queryset(self):
        return Review.objects.filter(pub_date__lte=timezone.now())

def about(request):
    return HttpResponse('This is the about page')
