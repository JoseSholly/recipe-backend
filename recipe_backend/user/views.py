from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from .serializers import CustomTokenObtainPairSerializer

User = get_user_model()
"""
# User Registration View: Django built auth-system
class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(email=email, password=password)
        # Create a token for the user (if using TokenAuthentication)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"message": "User created successfully", "token": token.key}, status=status.HTTP_201_CREATED)



# Logout View: Django built auth-system
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete the user's token to log them out (if using TokenAuthentication)
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)"""

class SignUpView(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(request_body=UserRegistrationSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            {
                "status": "error",
                "message": "Validation failed",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
# Login View: Django built auth-system
class LoginView(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        serializer = self.serializer_class(data=request.data)

        user = authenticate(email=email, password=password)
        if not user:
            return Response(
                {"error": "User .Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        print(data)
        return Response(data, status=status.HTTP_200_OK)       

class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated] 
    def post(self, request):
        refresh_token = request.data.get('refresh')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logged out successfully"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
