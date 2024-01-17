from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from .serializers import user_register_serializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user

# Create your views here.
class RegisterUserView(GenericAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class= user_register_serializer
    
    def post(self, request):
        user_data=request.data
        serializer=self.serializer_class(data=user_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
            send_code_to_user(user['email'])
            #send email function user['email]
            return Response({
                'data':user,
                'message':f'hi {user["first_name"]} tanks for signing up a passcode'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)