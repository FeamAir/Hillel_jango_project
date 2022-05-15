from django.shortcuts import render

from django.http import HttpResponseRedirect
from .models import Group
from django.views.decorators.csrf import csrf_exempt
from .forms import GroupCreateForm
from webargs.fields import Int, Str
from webargs.djangoparser import use_args


@use_args(
    {
        "language_groups": Str(required=False),
        "univer_subject": Str(required=False),
        "cnt_students": Int(required=False),
    },
    location="query"
)
def list_groups(request, args):
    gr = Group.objects.all()
    for key, value in args.items():
        gr = gr.filter(**{key: value})

    return render(
        request,
        "groups/list.html",
        {'title': "List of Groups", "groups": gr}
    )


@csrf_exempt
def create_groups(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

    return render(
        request,
        "groups/create.html",
        {'title': "Create new Groups", "form": form}
    )


@csrf_exempt
def update_groups(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

    return render(
        request,
        "groups/update.html",
        {'title': "Update Groups", "form": form}
    )
