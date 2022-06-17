from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import GroupBaseForm, GroupUpdateForm
from .models import Group


class CreateGroupsView(CreateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'
    form_class = GroupBaseForm


class DeleteGroupsView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/delete.html'


class ListGroupView(ListView):
    model = Group
    template_name = "groups/list.html"


class UpdateGroupView(UpdateView):
    model = Group
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'
    form_class = GroupUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group"] = self.get_object()

        return context
