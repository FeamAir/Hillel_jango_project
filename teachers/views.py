from django.shortcuts import render

from django.http import HttpResponse
from .models import Teacher
from .utils import qs2html
from webargs.fields import Int
from webargs.djangoparser import use_kwargs


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
