from ntpath import realpath
from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework import response, status, generics, permissions,views
from .serializer import LoginSerializer, updateProfile, RegisterSerializer, getUserProfile, getUserProjects, getUserDonations, updateProfile,EmailVerificationSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, authentication_classes
from .models import User
from projects.models import Projects, Donations
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from user import myjwt
from django.conf import settings
import jwt
from user import serializer
from django.http import HttpResponseRedirect
import re




# Create your views here.

############### Register api #################
class RegisterApiView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['confirm_password'] == serializer.validated_data['password']:
                serializer.save()
                user_data = serializer.data
                user = User.objects.get(email=user_data['email'])
                token = RefreshToken.for_user(user).access_token
                current_site = get_current_site(request).domain
                relativeLink = reverse('email-verify')
                absurl = 'http://'+current_site + \
                    relativeLink+"?token="+str(token)
                email_body = 'Hi '+user.first_name + \
                    ' Use the link below to verify your email \n' + absurl
                data = {'email_body': email_body, 'to_email': user.email,
                        'email_subject': 'Verify your email'}
                Util.send_email(data)
                return response.Response({'data':serializer.data,
                'status': 1
                }, status=status.HTTP_201_CREATED)
            return response.Response({"message_error": "password must match",
            'status': 0
            }, status=status.HTTP_400_BAD_REQUEST)

        return response.Response({'message_error': serializer.errors,
        'status': 0
        }, status=status.HTTP_400_BAD_REQUEST)


############## Activate Email #################
class verifyEmail(views.APIView):
    serializer_class=EmailVerificationSerializer
    def get(self,request):
        token=request.GET.get('token')
        try:
           payload=jwt.decode(token,settings.SECRET_KEY )
           print(payload)
           user=User.objects.get(id=payload['user_id'])
           if not user.is_verifications:
             user.is_verifications=True
             user.save()
             return HttpResponseRedirect(redirect_to='http://localhost:4200/login')
             
           else:
             return HttpResponseRedirect(redirect_to='http://localhost:4200/login')
             


        except jwt.ExpiredSignatureError as identifier:
                return response.Response({'message_error':'ACTIVATION LINK EXPIRED',
                'status': 0
                }, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
                return response.Response({'message_error':'invalid token', 
                'status':0
                
                }, status=status.HTTP_400_BAD_REQUEST)


##############  Login Api #################
class LoginApiView(GenericAPIView):
    serializer_class = LoginSerializer ##

    def post(self, request):
        email = request.data.get('email', None)
        confirm_password = request.data.get('password', None)
        try:
            password = User.objects.values_list('password').get(email=email)
            is_verified = User.objects.values_list(
                'is_verifications').get(email=email)
            is_verified2 = list(is_verified)
            str_password = ''.join(password)

            if check_password(confirm_password, str_password):
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    user = None
                if not is_verified2[0]:
                    return response.Response({'message_error': "please verify your email",
                    'status': 0
                    
                    }, status=status.HTTP_401_UNAUTHORIZED)

                if user:
                    serializer = self.serializer_class(user)
                    User.objects.filter(email=email).update(
                        is_authenticated=True)

                    return response.Response({'data':serializer.data,
                    'status': 1
                    }, status=status.HTTP_200_OK)

        except:
            password = None

        return response.Response({'message_error': "invalid credentials",
        'status': 0
        
        
        }, status=status.HTTP_401_UNAUTHORIZED)

#=======================================================================================#
#			                          view user profile                                	#
#=======================================================================================#


@api_view(['GET'])
# @authentication_classes([jwt.JWTAuthentication])
# @permission_classes([IsAuthenticated])
def user_profile(request, user_id):

    try:
        query = User.objects.get(id=user_id)
        serializer = getUserProfile(instance=query, read_only=True)
        serializer = ({
            "status": 1,
            "data": serializer.data
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:
        if User.DoesNotExist:
            serializer = ({
                "status": 0,
                "message": f"There is no user with this id = {user_id}",
            })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)

#=======================================================================================#
#                                   view user projects                                  #
#=======================================================================================#


@api_view(['GET'])
# @authentication_classes([jwt.JWTAuthentication])
# @permission_classes([IsAuthenticated])
def user_projects(request, user_id):
    try:
        query = Projects.objects.filter(owner_id=user_id).all()
        serializer = getUserProjects(query, many=True, read_only=True).data
        if len(serializer) > 0:
            serializer = (
                {
                    "status": 1,
                    "count": len(serializer),
                    "data": serializer
                })
        else:
            raise serializers.ValidationError("no data to show")
    except:
        if Projects.DoesNotExist:
            serializer = (
                {
                    "status": 0,
                    "message": f"There is no user with this id = {user_id}",
                })
    return Response(serializer)

#=======================================================================================#
#                                  view user Donations                                  #
#=======================================================================================#


@api_view(['GET'])
# @authentication_classes([jwt.JWTAuthentication])
# @permission_classes([IsAuthenticated])
def user_donations(request, user_id):
    try:
        query = Donations.objects.filter(user_id=user_id).all()
        serializer = getUserDonations(query, many=True, read_only=True).data
        if len(serializer) > 0:
            serializer = (
                {
                    "status": 1,
                    "count": len(serializer),
                    "data": serializer
                })
        else:
            raise serializers.ValidationError("no data to show")
    except:
        if Projects.DoesNotExist:
            serializer = (
                {
                    "status": 0,
                    "message": f"There is no donations with this user id = {user_id}",
                })
    return Response(serializer)

#=======================================================================================#
#                                  update  user Data                                    #
#=======================================================================================#


@api_view(['POST'])
# @authentication_classes([jwt.JWTAuthentication])
# @permission_classes([IsAuthenticated])
def update_user(request, user_id):
    query = User.objects.get(id=request.data['id'])
    serializer = updateProfile(instance=query, data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer = ({
            "status": 1,
            "message": "update Profile successfully",
            "date": serializer.data
        })
        return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)


#=======================================================================================#
#			                            delete user                                    	#
#=======================================================================================#

@api_view(['DELETE'])
# @authentication_classes([jwt.JWTAuthentication])
# @permission_classes([IsAuthenticated])
def delete_user(request, user_id):
    try:
        User.objects.get(id=user_id).delete()
        serializer = ({
            "status": 1,
            "message": "Deleted successfly",
        })
        return Response(serializer, status=status.HTTP_202_ACCEPTED)
    except:
        serializer = ({
            "status": 0,
            "message": f"There is no user with this id = {user_id}",
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)
