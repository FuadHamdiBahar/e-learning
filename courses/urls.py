from django.urls import path

from . import views

urlpatterns = [
    path('', views.CourseListCreateView.as_view(), name='ListCreateView'),
]