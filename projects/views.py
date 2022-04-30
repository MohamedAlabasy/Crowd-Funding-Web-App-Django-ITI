from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import createProjects, createComment


@api_view(['POST'])
def create_project(request):
    serializer = createProjects(data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer = ({
            "status": 1,
            "message": "Project created successfully",
            "date": serializer.data
        })
        return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        # serializer = ({
        #     "status": 0,
        #     "error": serializer.errors,
        # })
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#=======================================================================================#
#			                            Replies                                     	#
#=======================================================================================#


@api_view(['POST'])
def create_comment(request):
    serializer = createComment(data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer = ({
            "status": 1,
            "message": "Project created successfully",
            "date": serializer.data
        })
        return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
