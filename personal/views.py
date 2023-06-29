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

from rest_framework.response import Response
from rest_framework import status

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
    permission_classes = (
        # First check authentication
        IsAuthenticated,
        # Then check is admin or readonly.
        IsAdminOrReadOnly,
    )


class PersonalRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return self.update(request, *args, **kwargs)
        
        data = {
            'message': 'You are not authorized to update '
        }

        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # self.perform_destroy(instance)
        if self.request.user.is_superuser:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        data = {
            'message': 'You are not authorized to delete'
        }

        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    

# --------------------- NESTED VIEW ------------------- #
class DepartmentPersonalView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonalNestedSerializer
    permission_classes = (
        # First check authentication
        IsAuthenticated,
        # Then check is admin or readonly.
        IsAdminOrReadOnly,
    )

    def get_queryset(self):
        """
        Optionally restricts the returned department to a given one,
        by filtering against a `department` query parameter in the URL.
        """
        department = self.kwargs['department']
        if department is not None:
            return Department.objects.filter(name__iexact=department)

