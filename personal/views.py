from django.shortcuts import render
from .serializers import (
    DepartmentSerializer, 
    PersonalSerializer,
    DepartmentPersonalNestedSerializer
    )
from .models import Department, Personal
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    )

class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonalListCreateView(ListCreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer


class PersonalRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer


class DepartmentPersonalView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonalNestedSerializer

