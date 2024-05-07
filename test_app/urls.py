from django.urls import path
from .views import TestView,UserRegistrationView, ResultView, LoginView


urlpatterns = [
    path('register/' , UserRegistrationView.as_view()),
    path('auth/', LoginView.as_view()),
    path('test/', TestView.as_view()),
    path('test/<int:pk>/', TestView.as_view()),
    path('test/<str:q_type>/', TestView.as_view()),
    path('test/<str:q_type>/<str:q_subject>',TestView.as_view()),
    path('result/<int:pk>', ResultView.as_view()),
    path('result/', ResultView.as_view())
]