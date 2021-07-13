from django.urls import path, include
from .views import (
    RegisterAPIView, LoginAPIView, UserAPIView, LogoutAPIView, 
    ProfileInfoAPIView, ProfilePasswprdAPIView
)

urlpatterns = [
    path('register', RegisterAPIView.as_view()),   # http://localhost:8000/api/admin/register
    path('login', LoginAPIView.as_view()),   # http://localhost:8000/api/admin/login  
    path('user', UserAPIView.as_view()),   # http://localhost:8000/api/admin/user   
    path('logout', LogoutAPIView.as_view()),   # http://localhost:8000/api/admin/logout   
    path('users/info', ProfileInfoAPIView.as_view()),   # http://localhost:8000/api/admin/users/info 
    path('users/password', ProfilePasswprdAPIView.as_view()),   # http://localhost:8000/api/admin/users/password 

]


