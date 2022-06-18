from django.urls import path

from .views import CreateGroupsView
from .views import DeleteGroupsView
from .views import ListGroupView
from .views import UpdateGroupView

app_name = "groups"

urlpatterns = [

    path("", ListGroupView.as_view(), name='list'),
    path("create/", CreateGroupsView.as_view(), name='create'),
    path("update/<int:pk>/", UpdateGroupView.as_view(), name='update'),
    path("delete/<int:pk>/", DeleteGroupsView.as_view(), name="delete")

]
