
from django.shortcuts import render
from django.http import HttpResponse
from . import SaveToDatabase
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def userInfoStore(request):
    if request.method == "POST":
        emailAddress = request.body
        print(emailAddress)
        succes = SaveToDatabase.saveUserToDatabase(request.POST)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['emailAddress']
        print(content)
        # return HttpResponse(succes)
        return HttpResponse(request)
    else:
        return HttpResponse("PLEASE USE POST METHOD TO SEND DATA TO DATABASE.")

@csrf_exempt
def userExperienceStore(request):
    if request.method == "POST":
        succes = SaveToDatabase.saveExperienceToDatabase(request)
        return HttpResponse(succes)
    else:
        return HttpResponse("PLEASE USE POST METHOD TO SEND DATA TO DATABASE.")