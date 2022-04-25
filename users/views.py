from django.shortcuts import render
import json


from django.http import HttpResponse

# Create your views here.


def create_user(request):
    response = json.dumps([
        {
            "first_name": "Mohamed",
            "last_name": "Alabasy",
            "age": 24,
        },
        {
            "first_name": "Mohamed",
            "last_name": "Alabasy",
            "age": 24,
        },
    ])
    return HttpResponse(response, content_type='text/json')
