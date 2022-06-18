from django.urls import path

from .views import CreateStudentView
from .views import DeleteStudentsView
from .views import ListStudentsView
from .views import UpdateStudentView
from .views import generate_students


app_name = "students"

urlpatterns = [
    path("generate_students/", generate_students, name="random"),
    path('', ListStudentsView.as_view(), name='list'),
    path("create/", CreateStudentView.as_view(), name="create"),
    path("update/<int:pk>/", UpdateStudentView.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteStudentsView.as_view(), name="delete")
    ]
