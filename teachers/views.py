from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from webargs.djangoparser import use_args, use_kwargs
from webargs.fields import Int, Str

from .forms import TeacherCreateForm
from .models import Teacher
from .utils import qs2html


@use_kwargs(
    {
        "cnt": Int(required=False, missing=10)
    },
    location="query"
)
def generate_teachers(request, cnt):
    Teacher.gen_teachers(cnt)
    tc = Teacher.objects.all()
    html = qs2html(tc)
    return HttpResponse(html)


@use_args(
    {
        "first_name": Str(required=False),
        "last_name": Str(required=False),
        "age": Int(required=False),
    },
    location="query"
)
def list_teachers(request, args):
    tc = Teacher.objects.all()
    for key, value in args.items():
        tc = tc.filter(**{key: value})

    return render(
        request,
        "teachers/list.html",
        {'title': "List of Teachers", "teachers": tc}
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
