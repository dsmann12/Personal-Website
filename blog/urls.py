from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /blog/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /blog/about
    url(r'^about$', views.about, name='about')
]