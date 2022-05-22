"""universitety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teachers.views import generate_teachers
from teachers.views import list_teachers
from teachers.views import create_teachers
from groups.views import list_groups
from groups.views import create_groups

urlpatterns = [
    path('admin/', admin.site.urls),
    path("generate_teachers/", generate_teachers),
    path('teachers/', list_teachers),
    path("teachers/create", create_teachers),
    path("groups/", list_groups),
    path("groups/create", create_groups)
]
