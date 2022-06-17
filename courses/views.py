from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CourseBaseForm
from .models import Course


def create_course(request):
    if request.method == 'GET':
        form = CourseBaseForm()
    else:
        form = CourseBaseForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, "courses/create.html", {"form": form})


def list_course(request):
    courses = Course.objects.all()
    return render(request, "courses/list.html", {"courses": courses})


def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'GET':
        form = CourseBaseForm(instance=course)
    else:
        form = CourseBaseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, "courses/update.html", {"form": form})


def delete_course(request, pk):
    courses = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        courses.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/delete.html', {'courses': courses})
