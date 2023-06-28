from django.urls import path
from .views import (
    DepartmentListCreateView,
    DepartmentRUDView,
    PersonalListCreateView,
    PersonalRUDView,
    DepartmentPersonalView
    )

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view()),
    path('departments/<int:pk>/', DepartmentRUDView.as_view()),
    path('personals/', PersonalListCreateView.as_view()),
    # path('personals/<int:pk>/', PersonalRUDView.as_view()),
    path('department-personal-nested/<str:department>/', DepartmentPersonalView.as_view()),
]