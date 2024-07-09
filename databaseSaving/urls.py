from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import databaseSaving.views


urlpatterns = [
    path("userInfo/", databaseSaving.views.userInfoStore),
    path("userExperience/", databaseSaving.views.userExperienceStore),
]
