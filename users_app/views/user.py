"""
Views for the user API
"""
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from users_app.serializers import UserSerializer
from rest_framework import generics, authentication, permissions
from users_app.serializers import UserSerializer


class ListUsersView(generics.ListAPIView):
    """Listar todos os usuários (apenas para administradores)."""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieve and return the authenticated user.
        """
        return self.request.user
