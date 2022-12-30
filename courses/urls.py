from django.urls import path

from . import views

urlpatterns = [
    path('', views.CourseListCreateView.as_view(), name='ListCreateView'),
    path('<pk>/', views.CourseRetrieveUpdateDeleteView.as_view(), name='RetrieveUpdateDeleteView')
]