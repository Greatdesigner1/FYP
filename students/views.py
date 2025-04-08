from django.shortcuts import render
from rest_framework import viewsets
from students.models import Session, Student
from .serializers import SessionSreializer, SessionUpdateSerializer, StudentSerializer, StudentUpdateSerializer

# Create your views here.


class StudentsViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return StudentUpdateSerializer
        return super().get_serializer_class()


class SessionViewset(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSreializer
    http_method_names = ['post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return SessionUpdateSerializer
        return super().get_serializer_class()
