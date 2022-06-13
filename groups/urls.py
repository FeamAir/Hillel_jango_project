from django.urls import path

from .views import create_groups
from .views import delete_groups
from .views import list_groups
from .views import update_groups

app_name = "groups"

urlpatterns = [

    path("", list_groups, name='list'),
    path("create/", create_groups, name='create'),
    path("update/<int:pk>/", update_groups, name='update'),
    path("delete/<int:pk>/", delete_groups, name="delete")

]
