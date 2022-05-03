from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import updateDonateProjects, DonateToProject, createProjects, getTags, getSingleProject, getCategories, createComment, CommentReply, ReportProject, RateProjects, getProjects
from .models import Projects, Categories, Tags


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
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)


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
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)


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
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)


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
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)


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
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def cancel_project(request, project_id):
    try:
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
            serializer = ({
                "status": 1,
                "message": "You can't cancel this project because current donation more than 25%"
            })
            return Response(serializer, status=status.HTTP_404_NOT_FOUND)
    except:
        if Projects.DoesNotExist:
            serializer = (
                {
                    "status": 0,
                    "message": f"There is no project with this id = {project_id}",
                })
            return Response(serializer, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_categories(request):
    try:
        query = Categories.objects.all()
        serializer = getCategories(query, many=True, read_only=True).data
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
                    "message": "There is no data yet",
                })
    return Response(serializer)


@api_view(['GET'])
def get_all_tags(request):
    try:
        query = Tags.objects.all()
        serializer = getTags(query, many=True, read_only=True).data
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
                    "message": "There is no Tags to show",
                })
    return Response(serializer)


@api_view(['GET'])
def show_similar_project(request, project_id):
    try:
        query = Projects.objects.get(id=project_id)
        serializer = getSingleProject(query).data

        query_similar_project = Projects.objects.filter(
            tag=serializer['tag'][0]).all()[:4]
        serializer_similar_project = getSingleProject(
            query_similar_project, many=True).data
        serializer = ({
            "status": 1,
            "similar_project_count": len(serializer_similar_project),
            "project": serializer,
            'similar_project': serializer_similar_project,
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


@api_view(['GET'])
def show_project(request, project_id):
    try:
        query = Projects.objects.get(id=project_id)
        serializer = getProjects(query).data
        serializer = ({
            "status": 1,
            "data": serializer,
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:

        serializer = (
            {
                "status": 0,
                "message": f"There is no tags with this id = {project_id}",
            })
    return Response(serializer, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_latest_projects(request):
    try:
        query = Projects.objects.all().order_by('created_at').reverse()[:5]
        serializer = getProjects(query, many=True).data

        serializer = ({
            "status": 1,
            'projects': serializer,

        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:

        serializer = (
            {
                "status": 0,
                "message": "There is no projects to show",
            })
    return Response(serializer, status=status.HTTP_404_NOT_FOUND)


def update_donate_project(project_id, paid_up):
    # try:
    query = Projects.objects.get(id=project_id)
    # except:
    # serializer = (
    #         {
    #             "status": 0,
    #             "message": f"There is no project with this id = {project_id}"
    #         })
    #     return Response(serializer, status=status.HTTP_404_NOT_FOUND)
    data = {
        "current_donation": paid_up
    }
    print(project_id, paid_up)
    serializer = updateDonateProjects(instance=query, data=data)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
        serializer = ({
            "status": 1,
            "errors": "serializer.errors"
        })
        return Response(serializer)

    else:
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer)


@api_view(['POST'])
def donate_project(request, project_id):
    request.data['project'] = project_id
    serializer = DonateToProject(data=request.data)
    if serializer.is_valid():
        if request.data['paid_up'] == 0 or not request.data['paid_up']:
            serializer = ({
                "status": 0,
                "message": "You must enter any donate"
            })
            return Response(serializer, status=status.HTTP_404_NOT_FOUND)
        else:
            update_donate_project(project_id, request.data['paid_up'])
            serializer.save()
            serializer = ({
                "status": 1,
                "message": "Donate successfully",
                "date": serializer.data
            })
            return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)
