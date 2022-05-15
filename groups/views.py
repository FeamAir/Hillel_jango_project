from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from .models import Group
from django.views.decorators.csrf import csrf_exempt
from .forms import GroupCreateForm
from .utils import qs2html


def list_groups(request):
    gr = Group.objects.all()
    html = qs2html(gr)
    return HttpResponse(html)


@csrf_exempt
def create_groups(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    else:
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/groups/')

    html_form = f"""
        <form method="post">
            <table>
                {form.as_table()}
            </table>
            <input type="submit" value="Create">
        </form> 
        """

    return HttpResponse(html_form)
