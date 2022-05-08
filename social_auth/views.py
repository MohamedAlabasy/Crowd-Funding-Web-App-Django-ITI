from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import FacebookSocialAuthSerializer
from user.models import User
from . import  facebook
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
import jwt
from datetime import datetime, timedelta
from django.conf import settings


# Create your views here.
class FacebookSocialAuthView(GenericAPIView):

    serializer_class = FacebookSocialAuthSerializer

    def post(self, request):
   
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        auth_token = request.data['auth_token']
        ###################
        user_data = facebook.Facebook.validate(auth_token)
        try:
                email = user_data['email']
                first_name = user_data['first_name']
                last_name = user_data['last_name']
                Birth_date = user_data['birthday']
                facebook_profile = user_data['link']
                profile_image = user_data['picture']['data']['url']
                country = user_data['hometown']['name']
                provider = 'facebook'
                token = jwt.encode({'email': email,
                            'exp': datetime.utcnow()+timedelta(hours=24)},
                           settings.SECRET_KEY, algorithm='HS256')

                if User.objects.filter(email=email,auth_provider=provider):
                        # return HttpResponseRedirect(redirect_to='http://localhost:4200')
                        User.objects.filter(email=email,auth_provider=provider).update(last_login=datetime.now())
                        return Response({'message': 'you are already logged in','token':token,'status':1}, status=status.HTTP_200_OK)


                else:
                    User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=make_password('5f1ebb3260sssf643dd31131f1007'),
                        profile_image=profile_image,
                        country = country,
                        auth_provider = provider,
                        facebook_profile=facebook_profile,
                        is_verifications = True,
                        is_authenticated= True,
                        last_login=datetime.now()
                    )
            
        except Exception as identifier:

                return Response({'message_error': 'token is invalid or expired login again','status':0}, status=status.HTTP_200_OK)


        return Response({'message':'login successfully','token': token,'status':1}, status=status.HTTP_200_OK)
