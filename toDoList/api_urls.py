from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from api_views import TaskCreateAPIView, TaskDeleteAPIView, TaskAllAPIView, TaskCompletedAPIView

urlpatterns = [
    url(r'^task/create/$', TaskCreateAPIView.as_view()),
    url(r'^task/delete/$', TaskDeleteAPIView.as_view()),
    url(r'^task/get/all/$', TaskAllAPIView.as_view()),
    url(r'^task/get/completed/$', TaskCompletedAPIView.as_view()),
    url(r'^task/completed/$', TaskCompletedAPIView.as_view()),
]