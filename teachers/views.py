from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import Teacher
from .utils import qs2html
from webargs.fields import Int, Str
from webargs.djangoparser import use_kwargs, use_args
from django.views.decorators.csrf import csrf_exempt
from .forms import TeacherCreateForm


def index(request):
    return render(request, "teachers/index.html")


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


@csrf_exempt
def create_teachers(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/teachers/')

    return render(
        request,
        "teachers/create.html",
        {'title': "Create new Teacher", "form": form}
    )


@csrf_exempt
def update_teachers(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    else:
        form = TeacherCreateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/teachers/')

    return render(
        request,
        "teachers/update.html",
        {'title': "Update Teacher", "form": form}
    )
