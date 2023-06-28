from django.urls import path
from .views import (
    DepartmentListCreateView,
    DepartmentRUDView,
    PersonalListCreateView,
    PersonalRUDView
    )

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view()),
    path('departments/<int:pk>/', DepartmentRUDView.as_view()),
    path('personals/', PersonalListCreateView.as_view()),
    path('personals/<int:pk>/', PersonalRUDView.as_view()),
]