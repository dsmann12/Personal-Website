# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    # prevents posts with a pub_date in future from showing
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    # exclude posts that aren't published yet
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

def about(request):
    return HttpResponse('This is the about page')
