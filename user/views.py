from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import response,status

from .serializer import RegisterSerializer


# Create your views here.
class RegisterApiView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self,request):
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['confirm_password']==serializer.validated_data['password']:
        
                serializer.save()
                return response.Response(serializer.data,status=status.HTTP_201_CREATED)
            return response.Response({"password_error":"password must match"},status=status.HTTP_400_BAD_REQUEST)
            
        return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)