from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import TeacherCreateForm
from .forms import TeacherFilterForm
from .models import Teacher


def generate_teachers(request):
    Teacher.gen_teachers()
    return HttpResponseRedirect(reverse('teachers:list'))


def list_teachers(request):
    teachers = Teacher.objects.all()
    teachers_filter = TeacherFilterForm(data=request.GET, queryset=teachers)

    return render(
        request,
        "teachers/list.html",
        {'teachers_filter': teachers_filter}
    )


def create_teachers(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, "teachers/create.html", {"form": form})


def update_teachers(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    else:
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, "teachers/update.html", {"form": form})


def delete_teachers(request, pk):
    teachers = get_object_or_404(Teacher, pk=pk)

    if request.method == "POST":
        teachers.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {'teachers': teachers})
