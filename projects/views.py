from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework import serializers, status
from user import myjwt
from .serializers import AddProjectsPictures, getComments, ProjectsTags, ProjectsSearchBarTags, ProjectsPictures, updateDonateProjects, DonateToProject, createProjects, getTags, getSingleProject, getCategories, createComment, CommentReply, ReportProject, ReportsComment, updateRateProjects, RateProjects, getProjects
from .models import Projects, Categories, Tags, Rates, Pictures, Comments

#=======================================================================================#
#			                       create_project                                       #
#=======================================================================================#
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_project_images(images, project_id):
    for image in images:
        data = ({
            "project": project_id,
            "image": image
        })
        serializer = AddProjectsPictures(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            serializer = ({
                "status": 0,
                "errors": serializer.errors
            })
            return Response(serializer, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = ({
            "status": 1,
            "message": "pictures added successfully",
        })
        return Response(serializer, status=status.HTTP_201_CREATED)


@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_project_tags(tags, project_id):
    print(tags)
    for tag in tags:
        data = ({
            "project": project_id,
            "tag": tag,
        })
        serializer = ProjectsTags(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            serializer = ({
                "status": 0,
                "errors": serializer.errors
            })
            return Response(serializer, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = ({
            "status": 1,
            "message": "tag added successfully",
        })
        return Response(serializer, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_project(request):
    if not request.FILES.getlist('images'):
        serializer = ({
            "status": 0,
            "errors": {
                "images": "This field is required"
            }
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)
    if not request.POST.getlist('tags'):
        serializer = ({
            "status": 0,
            "errors": {
                "tags": "This field is required"
            }
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)
    data = ({
        "title": request.data['title'],
        "details": request.data['details'],
        "rate": 0,
        "current_donation": 0,
        "total_target": request.data['total_target'],
        "end_campaign": request.data['end_campaign'],
        "category": request.data['category'],
        "owner": request.data['owner'],
    })
    serializer = createProjects(data=data)
    if serializer.is_valid():
        ob = serializer.save()
        print(ob.id)
        add_project_images(request.FILES.getlist('images'), ob.id)
        add_project_tags(request.POST.getlist('tags'), ob.id)
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

#=======================================================================================#
#			                        create_comment                                      #
#=======================================================================================#


@api_view(['POST'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
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

#=======================================================================================#
#			                       reply_comment                                        #
#=======================================================================================#


@api_view(['POST'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
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

#=======================================================================================#
#			                        report_project                                      #
#=======================================================================================#


@api_view(['POST'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
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

#=======================================================================================#
#			                          report_comment                                    #
#=======================================================================================#


@api_view(['POST'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
def report_comment(request):
    serializer = ReportsComment(data=request.data)
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

#=======================================================================================#
#			                            rate                                         	#
#=======================================================================================#


@api_view(['POST'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
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

#=======================================================================================#
#			                          cancel_project                                    #
#=======================================================================================#


@api_view(['DELETE'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
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

#=======================================================================================#
#			                         all_categories                                     #
#=======================================================================================#


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

#=======================================================================================#
#			                       get_all_tags                                         #
#=======================================================================================#


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

#=======================================================================================#
#			                           show_project                                     #
#=======================================================================================#


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

#=======================================================================================#
#			                     get_latest_projects                                   	#
#=======================================================================================#


@api_view(['GET'])
def get_latest_projects(request):
    try:
        query = Projects.objects.all().order_by('created_at').reverse()[:5]
        serializer = getProjects(query, many=True).data
        serializer = ({
            "status": 1,
            'count': len(serializer),
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

#=======================================================================================#
#			                            donate_project                                  #
#=======================================================================================#


def update_donate_project(project_id, paid_up):
    query = Projects.objects.get(id=project_id)
    if paid_up + query.current_donation > query.total_target:
        serializer = ({
            "status": 0,
            "message": f"You cannot donate more than {query.total_target-query.current_donation} to this project",
        })
        raise serializers.ValidationError(serializer)
    data = {
        "current_donation": paid_up + query.current_donation
    }
    serializer = updateDonateProjects(instance=query, data=data)
    if serializer.is_valid():
        serializer.save()
        return
    else:
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        raise serializers.ValidationError(serializer)


@api_view(['POST'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
def donate_project(request):
    serializer = DonateToProject(data=request.data)
    if serializer.is_valid():
        if request.data['paid_up'] == 0 or not request.data['paid_up']:
            serializer = ({
                "status": 0,
                "message": "You must enter any donate"
            })
            return Response(serializer, status=status.HTTP_404_NOT_FOUND)
        else:
            update_donate_project(
                request.data['project'], request.data['paid_up'])
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

#=======================================================================================#
#			                        rate_project                                       	#
#=======================================================================================#


@api_view(['POST'])
@authentication_classes([myjwt.JWTAuthentication])
@permission_classes([IsAuthenticated])
def rate_project(request):
    serializer = RateProjects(data=request.data)
    if serializer.is_valid():
        if request.data['rate'] > 5 or request.data['rate'] < 0:
            serializer = ({
                "status": 0,
                "message": "You must enter rate only between 0 and 5"
            })
            return Response(serializer, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer.save()
            update_rate_project(request.data['rate'], request.data['project'])
            serializer = ({
                "status": 1,
                "message": "Rated successfully",
                "date": serializer.data
            })
            return Response(serializer, status=status.HTTP_201_CREATED)
    else:
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)


def update_rate_project(current_rate, project_id):
    project_query = Projects.objects.get(id=project_id)

    rate_query = Rates.objects.filter(project_id=project_id).all()
    total_rates = RateProjects(rate_query, many=True).data

    user_rate = 0
    for rate in total_rates:
        user_rate = user_rate + rate['rate']

    rate_value = 0
    if len(total_rates) == 0:
        rate_value = round(current_rate/(1 * 5)*5)
    else:
        rate_value = round(user_rate/(len(total_rates)*5)*5)
    data = {
        "rate": rate_value
    }
    serializer = updateRateProjects(instance=project_query, data=data)
    if serializer.is_valid():
        serializer.save()
        return
    else:
        serializer = ({
            "status": 0,
            "errors": serializer.errors
        })
        raise serializers.ValidationError(serializer)


#=======================================================================================#
#			                           all_project                                      #
#=======================================================================================#
@api_view(['GET'])
def all_project(request):
    try:
        query = Projects.objects.all()
        serializer = getProjects(query, many=True).data
        serializer = ({
            "status": 1,
            "count": len(serializer),
            "data": serializer,
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:
        serializer = (
            {
                "status": 0,
                "message": 'no projects to show',
            })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)

#=======================================================================================#
#			                            project_category                                #
#=======================================================================================#


@api_view(['GET'])
def project_category(request, category_id):
    try:
        query = Projects.objects.filter(category_id=category_id).all()
        serializer = getProjects(query, many=True).data
        serializer = ({
            "status": 1,
            "data": serializer,
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:
        serializer = (
            {
                "status": 0,
                "message": f"There is no category with this id = {project_id}",
            })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)

#=======================================================================================#
#			                       search_bar_title                                     #
#=======================================================================================#


@api_view(['GET'])
def search_bar_title(request, project_title):
    try:
        query = Projects.objects.get(title=project_title)
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
                "message": f"There is no match with this title = {project_title}",
            })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)

#=======================================================================================#
#			                            rate                                         	#
#=======================================================================================#


@api_view(['GET'])
def search_bar_tag(request, project_tag):
    try:
        query = Tags.objects.filter(tag=project_tag).all()
        serializer = ProjectsSearchBarTags(query, many=True).data
        serializer = ({
            "status": 1,
            'count': len(serializer),
            "data": serializer,
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:
        serializer = (
            {
                "status": 0,
                "message": f"There is no projects match with this tag = {project_tag}",
            })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)

#=======================================================================================#
#			                            highest_rate                                    #
#=======================================================================================#


@api_view(['GET'])
def highest_rate(request):
    try:
        query = Projects.objects.all().order_by('rate').reverse()[:5]
        serializer = getProjects(query, many=True).data
        serializer = ({
            "status": 1,
            'count': len(serializer),
            "data": serializer,
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:
        serializer = (
            {
                "status": 0,
                "message": "There is no rate match with this hightest rate projects"
            })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)

#=======================================================================================#
#			                       latest_admin_selected                                #
#=======================================================================================#


@api_view(['GET'])
def latest_admin_selected(request):
    try:
        query = Projects.objects.all().order_by(
            'selected_at_by_admin').reverse()[:5]
        serializer = getProjects(query, many=True).data
        serializer = ({
            "status": 1,
            'count': len(serializer),
            "data": serializer,
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:
        serializer = (
            {
                "status": 0,
                "message": "There is no projects match with this time"
            })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)

#=======================================================================================#
#			                            all_comments                                   	#
#=======================================================================================#


@api_view(['GET'])
def all_comments(request, project_id):
    try:
        query = Comments.objects.filter(project_id=project_id).all()
        serializer = getComments(query, many=True).data
        serializer = ({
            "status": 1,
            'count': len(serializer),
            "data": serializer
        })
        return Response(serializer, status=status.HTTP_200_OK)
    except:
        serializer = (
            {
                "status": 0,
                "message": "There is no Comments to show"
            })
        return Response(serializer, status=status.HTTP_404_NOT_FOUND)
