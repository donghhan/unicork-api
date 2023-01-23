from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "mobie_phone_number",
            "first_name",
            "last_name",
            "is_active",
        ]
