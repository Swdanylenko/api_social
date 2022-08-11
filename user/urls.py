from django.urls import path
from api import views

urlpatterns = [
    path('register', views.UserRegisterAPIView.as_view(), name='register'),
    path('login', views.UserLoginAPIView.as_view(), name='login'),
    path('', views.UserActivityAPIView.as_view()),
    ]