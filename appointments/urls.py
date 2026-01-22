from django.urls import path
from .views import *

urlpatterns = [
    path("", appointment_list, name="appointment_list"),
    path("create/", appointment_create, name="appointment_create"),
    path("<int:id>/manage/", appointment_manage, name="appointment_manage"),
]
