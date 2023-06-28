from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonalSerializer
from .models import Department, Personal
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class DepartmentListView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreateUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

