from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view()),   # http://localhost:8000/api/admin/register
    path('login', LoginAPIView.as_view()),   # http://localhost:8000/api/admin/login  
]


