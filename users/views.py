from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get_object(self):
        try:
            user = User.objects.all()
        except User.DoesNotExist:
            raise NotFound
        return user

    # View all users
    def get(self, request):
        serializer = UserSerializer(self.get_object(), many=True)
        return Response(serializer.data)

    # Create new users
    def post(self, request):
        serializer_new_user = UserSerializer(data=request.data)
        if serializer_new_user.is_valid():
            serializer_new_user.save()
            return Response(UserSerializer(serializer_new_user))
        else:
            return Response(serializer_new_user.errors)


class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound
        return user

    # View single user
    def get(self, request, pk):
        serializer = UserSerializer(self.get_object(pk))
        return Response(serializer.data)

    # Update single user
    def put(self, request, pk):
        serializer = UserSerializer(
            self.get_object(pk), data=request.data, partial=True
        )

        if serializer.is_valid():
            updated_user = serializer.save()
            return Response(UserSerializer(updated_user).data)

    # Delete single user
    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(HTTP_204_NO_CONTENT)
