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

from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (
        # First check authentication
        IsAuthenticated,
        # Then check is admin or readonly.
        IsAdminOrReadOnly,
    )


class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonalListCreateView(ListCreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer


class PersonalRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer

# --------------------- NESTED VIEW ------------------- #
class DepartmentPersonalView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonalNestedSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned department to a given one,
        by filtering against a `department` query parameter in the URL.
        """
        department = self.kwargs['department']
        if department is not None:
            return Department.objects.filter(name__iexact=department)

