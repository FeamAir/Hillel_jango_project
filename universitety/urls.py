from core.views import index

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path("teachers/", include('teachers.urls')),
    path("groups/", include('groups.urls')),
    path("students/", include('students.urls')),
    path("accounts/", include('accounts.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    path("courses/", include('courses.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
