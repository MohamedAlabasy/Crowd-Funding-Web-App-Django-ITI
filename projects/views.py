from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import createProjects,getSingleProject, createComment, CommentReply, ReportProject, RateProjects, getProjects
from .models import Projects


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
            "message": "comment created successfully",
            "date": serializer.data
        })
        return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def reply_comment(request):
    serializer = CommentReply(data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer = ({
            "status": 1,
            "message": "reply created successfully",
            "date": serializer.data
        })
        return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def report_project(request):
    serializer = ReportProject(data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer = ({
            "status": 1,
            "message": "report created successfully",
            "date": serializer.data
        })
        return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def rate_project(request, project_id):
    query = Projects.objects.get(id=project_id)
    serializer = RateProjects(instance=query, data=request.data)
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


@api_view(['DELETE'])
def cancel_project(request, project_id):
    query = Projects.objects.get(id=project_id)
    serializer = getProjects(query).data
    if (serializer['current_donation'] / serializer['total_target'] < 0.25):
        query.delete()
        serializer = ({
            "status": 1,
            "message": "Cancel successfully",
        })
        return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        raise serializers.ValidationError(
            "You can't cancel this project because current donation more than 25%")


@api_view(['GET'])
def show_similar_project(request, project_id):
    try:
        query = Projects.objects.get(id=project_id)
        serializer = getSingleProject(query).data
        #query2 = Projects.objects.get(tag=serializer['tag'])
        #serializer2 = getSingleProject(query2).data
        print(serializer['tag'][0])
        serializer = ({
            "status": 1,
            "project": serializer,
            #'similar project':serializer2,
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:

        serializer = ([
            {
                "status": 0,
                "message": f"There is no tags with this id = {project_id}",
            }
        ])
    return Response(serializer, status=status.HTTP_404_NOT_FOUND)
