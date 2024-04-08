from django.urls import path, include
from .views import AttendanceStatsView

urlpatterns = [
    path('stats/', AttendanceStatsView.as_view(), name="AttendanceStatsView"),
]