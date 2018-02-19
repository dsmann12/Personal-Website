from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'blog'

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /blog/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /blog/about
    url(r'^about$', TemplateView.as_view(template_name="blog/about.html"), name='about'),
    url(r'^games$', TemplateView.as_view(template_name="blog/games.html"), name='games'),
    url(r'^games/pong$', TemplateView.as_view(template_name="blog/pong.html"), name='pong'),
]