from django.shortcuts import render

from rest_framework import generics, status, mixins
from rest_framework.response import Response
# Create your views here.

from .models import Course
from .serializers import CourseSerializer

class CourseListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CourseRetrieveUpdateDeleteView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)