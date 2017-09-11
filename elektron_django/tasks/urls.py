from django.conf.urls import url

from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^datatask/(?P<pk>[0-9]+)/$', views.DataTaskDetailView.as_view(), name='datatask_detail'),
    url(r'^datetimetask/(?P<pk>[0-9]+)/$', views.DateTimeTaskDetailView.as_view(), name='datatimetask_detail'),
    url(r'^create$', csrf_exempt(views.CreateView.as_view()), name='create'),
    url(r'^devices$', csrf_exempt(views.TaskDeviceView.as_view()), name='devices'),
]