from django.urls import path

from .views import CreateTeachersView
from .views import DeleteTeachersView
from .views import ListTeachersView
from .views import UpdateTeacherView
from .views import generate_teachers


app_name = "teachers"

urlpatterns = [
    path("generate_teachers/", generate_teachers, name="random"),
    path('', ListTeachersView.as_view(), name='list'),
    path("create/", CreateTeachersView.as_view(), name="create"),
    path("update/<int:pk>/", UpdateTeacherView.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteTeachersView.as_view(), name="delete")
]
