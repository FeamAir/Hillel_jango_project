from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import Teacher
from .utils import qs2html
from webargs.fields import Int
from webargs.djangoparser import use_kwargs
from django.views.decorators.csrf import csrf_exempt
from .forms import TeacherCreateForm


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

def list_teachers(request):
    tc = Teacher.objects.all()
    html = qs2html(tc)
    return HttpResponse(html)

@csrf_exempt
def create_teachers(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    else:
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/teachers/')

    html_form = f"""
        <form method="post">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Create">
        </form> 
        """

    return HttpResponse(html_form)
