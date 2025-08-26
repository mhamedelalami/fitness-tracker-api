from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
from django.urls import get_resolver

def home(request):
    return render(request, "home.html")

def api_home(request):
    resolver = get_resolver()
    patterns = resolver.url_patterns
    endpoints = []

    def extract_patterns(patterns, prefix=''):
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):
                # Include nested patterns (like in admin or other apps)
                extract_patterns(pattern.url_patterns, prefix + getattr(pattern, 'pattern', '').regex.pattern)
            else:
                path_str = prefix + str(pattern.pattern)
                name = pattern.name if pattern.name else "no-name"
                endpoints.append({"path": "/" + path_str.strip("/"), "name": name})

    extract_patterns(patterns)
    return render(request, "api_home.html", {"endpoints": endpoints})

# User registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "Registration successful", "user": UserSerializer(user).data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Registration failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

# Current authenticated user profile
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Custom login view using authenticate() and JWT
class CustomLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
