from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def list_users(request):
    try:
        response = ([
            {
                "first_name": "Mohamed",
                "last_name": "Alabasy",
                "age": 24
            },
            {
                "first_name": "mona",
                "last_name": "ahmed",
                "age": 22
            }
        ])
    except:
        response = ([
            {
                "msg": "No Data To show",
            }
        ])
    return Response(response)


@csrf_exempt
@api_view(['POST'])
def create_user(request):
    body_data = request.data
    try:
        response = ([
            body_data
        ])
    except:
        response = ([
            {
                "msg": "No Data To show",
            }
        ])
    return Response(response)
