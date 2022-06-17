from core.views import index

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path("teachers/", include('teachers.urls')),
    path("groups/", include('groups.urls')),
    path("students/", include('students.urls')),
    path("courses/", include('courses.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
