from django.shortcuts import render, get_object_or_404

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Group

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

    return render(request, "groups/list.html", {"groups": gr})



def create_groups(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, "groups/create.html", {"form": form})



def update_groups(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    else:
        form = GroupCreateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, "groups/update.html", {"form": form})


def delete_groups(request, pk):
    groups = get_object_or_404(Group, pk=pk)

    if request.method == "POST":
        groups.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'groups': groups})
