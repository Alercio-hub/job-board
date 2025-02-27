from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from users_app.serializers import UserSerializer

class ListUsersView(generics.ListAPIView):
    """Lista todos os usuários (apenas para administradores)."""
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
