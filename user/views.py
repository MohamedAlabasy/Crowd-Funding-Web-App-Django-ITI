from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from .serializer import RegisterSerializer, getUserProfile, getUserProjects, getUserDonations, updateProfile

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from projects.models import Projects, Donations


# Create your views here.
class RegisterApiView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if serializer.validated_data['confirm_password'] == serializer.validated_data['password']:

                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response({"password_error": "password must match"}, status=status.HTTP_400_BAD_REQUEST)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#=======================================================================================#
#			                          view user profile                                	#
#=======================================================================================#

@api_view(['GET'])
def user_profile(request, user_id):
    try:
        query = User.objects.get(id=user_id)
        serializer = getUserProfile(query, read_only=True).data
        serializer = ({
            "status": 1,
            "data": serializer
        })
    except:
        if User.DoesNotExist:
            serializer = ({
                "status": 0,
                "message": f"There is no user with this id = {user_id}",
            })
    return Response(serializer)

#=======================================================================================#
#                                   view user projects                                  #
#=======================================================================================#


@api_view(['GET'])
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
                    "message": f"There is no user with this id = {user_id}",
                })
    return Response(serializer)

#=======================================================================================#
#                                  update  user Data                                    #
#=======================================================================================#


@api_view(['POST'])
def update_user(request, user_id):
    query = User.objects.get(id=user_id)
    serializer = updateProfile(instance=query, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


#=======================================================================================#
#			                            delete user                                    	#
#=======================================================================================#

@api_view(['DELETE'])
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
            "message": "NOT FOUND",
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)
