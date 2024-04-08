from django.urls import path, include
from .views import CourseStudent

urlpatterns = [
    path('getStudent/', CourseStudent.as_view(), name="getStudent"),
]