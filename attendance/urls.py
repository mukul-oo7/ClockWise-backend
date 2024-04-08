from django.urls import path, include
from .views import CourseStudent, HandleAttendance, LeaveApproved

urlpatterns = [
    path('getStudent/', CourseStudent.as_view(), name="getStudent"),
    path('uploadAttendance/', HandleAttendance.as_view(), name="HandleAttendance"),
    path('approve-leave/', LeaveApproved.as_view(), name="leave-approved"),

]