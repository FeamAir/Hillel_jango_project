from django.urls import path

from .views import create_course
from .views import delete_course
from .views import list_course
from .views import update_course


app_name = "courses"

urlpatterns = [

    path("", list_course, name='list'),
    path("create/", create_course, name='create'),
    path("update/<int:pk>/", update_course, name='update'),
    path("delete/<int:pk>/", delete_course, name="delete")

]
