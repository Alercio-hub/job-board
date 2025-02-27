"""
URL mappings for the user API.
"""
from django.urls import path
from .views import ListUsersView, CreateUserView, ManageUserView

app_name = 'users_app'

urlpatterns = [
    path('', ListUsersView.as_view(), name='list'),
    path('create/', CreateUserView.as_view(), name='create'),
    path('me/', ManageUserView.as_view(), name='me'),
]