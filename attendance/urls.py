from django.urls import path, include
from .views import CourseStudent, HandleAttendance

urlpatterns = [
    path('getStudent/', CourseStudent.as_view(), name="getStudent"),
    path('uploadAttendance/', HandleAttendance.as_view(), name="HandleAttendance"),
]