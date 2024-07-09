from django.contrib import admin
from django.urls import path
import databaseSaving.views

urlpatterns = [
    path("userInfo/", databaseSaving.views.userInfoStore),
]
