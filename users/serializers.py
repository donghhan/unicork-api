from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_admin",
            "last_login",
        ]
