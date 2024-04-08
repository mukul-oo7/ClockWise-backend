from django.urls import path, include
from .views import LoginView, RegisterView, RegisterCourse

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('register_course/', RegisterCourse.as_view(), name="register_course"),
]