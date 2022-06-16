from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import GroupBaseForm, GroupUpdateForm
from .models import Group


def create_groups(request):
    if request.method == 'GET':
        form = GroupBaseForm()
    else:
        form = GroupBaseForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, "groups/create.html", {"form": form})


def delete_groups(request, pk):
    groups = get_object_or_404(Group, pk=pk)

    if request.method == "POST":
        groups.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'groups': groups})


def list_groups(request):
    groups = Group.objects.all().select_related("course_group")
    return render(request, "groups/list.html", {"groups": groups})


def update_groups(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupUpdateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupUpdateForm(instance=group)

    return render(
        request,
        "groups/update.html",
        {"form": form, "group": group}
    )
