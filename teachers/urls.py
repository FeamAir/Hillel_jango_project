from django.urls import path

from .views import create_teachers
from .views import delete_teachers
from .views import generate_teachers
from .views import list_teachers
from .views import update_teachers


app_name = "teachers"

urlpatterns = [
    path("generate_teachers/", generate_teachers),
    path('', list_teachers, name='list'),
    path("create/", create_teachers, name="create"),
    path("update/<int:pk>/", update_teachers, name="update"),
    path("delete/<int:pk>/", delete_teachers, name="delete")
]
