from django.urls import path
from post import views

urlpatterns = [
    path('', views.PostsView.as_view(), name='post_view'),
    path('create', views.PostCreateView.as_view(), name='post_create'),
    path('vote', views.PostVoteView.as_view(), name='post_view'),
    path('analitics/', views.PostAnalitics.as_view(), name='analitics')
    ]