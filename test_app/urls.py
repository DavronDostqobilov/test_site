from django.urls import path
from .views import TestView,UserRegistrationView


urlpatterns = [
    path('register/' , UserRegistrationView.as_view()),
    path('test/', TestView.as_view()),
    path('test/<int:pk>/', TestView.as_view()),
    path('test/<str:q_type>/', TestView.as_view()),
    path('test/<str:q_type>/<str:q_subject>',TestView.as_view())
]