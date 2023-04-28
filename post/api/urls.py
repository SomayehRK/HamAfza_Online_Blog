from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostApiView.as_view(), name='post_list'),
    path('create/', views.PostCreateAPI.as_view(), name='post_create'),
    path('detail/<int:pk>', views.PostDetailAPI.as_view(), name='post_detail'),

]