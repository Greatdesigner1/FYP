from rest_framework import views, status
from .serializers import LoginUserSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(views.APIView):
    permission_classes = []
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        
        return Response({
            "message": "Logged in successfully",
            "tokens": {
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        }, status=status.HTTP_200_OK)


class ChangePasswordView(views.APIView):
    serializer_class = ChangePasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)

        user = request.user
        user.set_password(serializer.validated_data['new_password'])
        user.save()

        return Response({
            "message": "Password changed successfully"
        }, status=status.HTTP_200_OK)