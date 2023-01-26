from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


@api_view(["GET", "POST"])
def all_user_view(request):
    all_users = User.objects.all()
    serializer = UserSerializer(all_users, many=True)
    return Response(serializer.data)
