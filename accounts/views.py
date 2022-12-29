from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .tokens import create_jwt_pair_for_user
from .serializers import SignUpSerializer

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            
            response = {
                'message': 'User created successfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(generics.GenericAPIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            tokens = create_jwt_pair_for_user(user=user)
            response = {
                'message': 'Login Successfully',
                'tokens': tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)
        
        return Response(data={'message': 'Invalid email or password'}, status=status.HTTP_403_FORBIDDEN)

    
    def get(self, request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK)