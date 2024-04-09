from django.urls import path, include
from .views import LoginView, AppliedLeaveView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('leaveRequest/', AppliedLeaveView.as_view()),

]