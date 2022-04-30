from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from .serializer import RegisterSerializer, getUserProfile, getUserProjects, getUserDonations

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
        response = getUserProfile(query, read_only=True).data,
    except:
        if User.DoesNotExist:
            response = ([
                {
                    "message": f"There is no user with this id = {user_id}",
                }
            ])
        else:
            response = ([
                {
                    "message": "no data to show",
                }
            ])

    return Response(response)

#=======================================================================================#
#                                   view user projects                                  #
#=======================================================================================#


@api_view(['GET'])
def user_projects(request, user_id):
    try:
        query = Projects.objects.filter(owner_id=user_id).all()
        response = getUserProjects(
            query, many=True, read_only=True).data,
    except:
        if Projects.DoesNotExist:
            response = ([
                {
                    "message": f"There is no user with this id = {user_id}",
                }
            ])
        else:
            response = ([
                {
                    "message": "no data to show",
                }
            ])

    return Response(response)

#=======================================================================================#
#                                  view user Donations                                  #
#=======================================================================================#


@api_view(['GET'])
def user_donations(request, user_id):
    try:
        query = Donations.objects.filter(user_id=user_id).all()
        response = getUserDonations(
            query, many=True, read_only=True).data,
    except:
        if Projects.DoesNotExist:
            response = ([
                {
                    "message": f"There is no user with this id = {user_id}",
                }
            ])
        else:
            response = ([
                {
                    "message": "no data to show",
                }
            ])

    return Response(response)

#=======================================================================================#
#                                  update_user user Data                                #
#=======================================================================================#


# @api_view(['POST'])
# def update_user(request, user_id):
#     # try:
#     query = User.objects.get(id=user_id)
    # response = getUserProfile(data=request.data)
    # response = request.data
    # if response.is_valid():
    #     response.save()
    # except:
    # return Response(status=status.HTTP_404_NOT_FOUND)
    # if User.DoesNotExist:
    #     response = ([
    #         {
    #             "message": f"There is no user with this id = {user_id}",
    #         }
    #     ])
    # else:
    #     response = ([
    #         {
    #             "message": "no data to show",
    #         }
    #     ])

    # if request.method == 'PUT':
    # serializer = getUserProfile(instance=query, data=request.POST)
    # serializer = request.data
    # serializer.save()
    # serializer.save()
    # print(serializer.is_valid())
    # if serializer.is_valid():
    #     serializer.save()
    #     serializer = ([
    #         {
    #             "message": "SSS",
    #         }
    #     ])
    #     return Response(serializer)
    # return Response(serializer.data)


#=======================================================================================#
#			                            getUserDonations                               	#
#=======================================================================================#

@api_view(['DELETE'])
def delete_user(request, user_id):
    User.objects.get(id=user_id).delete()
    serializer = ([
        {
            "message": "SSS",
        }
    ])
    return Response(serializer)
