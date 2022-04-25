from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from django.http import HttpResponse

# Create your views here.


def list_users(request):
    if request.method == 'GET':
        try:
            response = json.dumps([
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
            response = json.dumps([
                {
                    "msg": "No Data To show",
                }
            ])
    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        body_data = json.loads(request.body)
        name = body_data['name']
        try:
            response = json.dumps([
                {
                    "name": name
                }
            ])
        except:
            response = json.dumps([
                {
                    "msg": "No Data To show",
                }
            ])
    return HttpResponse(response, content_type='text/json')
