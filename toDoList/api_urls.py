from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from api_views import TaskCreateAPIView, TaskDeleteAPIView, TaskAPIView

urlpatterns = [
    url(r'^create/$', TaskCreateAPIView.as_view()),
    url(r'^create/$', TaskDeleteAPIView.as_view()),
    url(r'^get-tasks/$', TaskAPIView.as_view()),

]