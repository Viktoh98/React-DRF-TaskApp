from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView


class CustomAuthPermissionsMixin(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
