# myapp/urls.py

from django.urls import path
from .views import RegistrationAPIView, LoginAPIView,UserRetrieveUpdateDestroyView,UserListCreateView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
]
