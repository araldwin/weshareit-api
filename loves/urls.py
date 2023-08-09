from django.urls import path
from loves import views

urlpatterns = [
    path('loves/', views.LoveList.as_view()),
    path('loves/<int:pk>/', views.LoveDetail.as_view()),
]