from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import TeacherCreateForm
from .forms import TeacherFilterForm
from .models import Teacher


def generate_teachers(request):
    Teacher.gen_teachers()
    return HttpResponseRedirect(reverse('teachers:list'))


class ListTeachersView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    paginate_by = 8

    def get_filter(self):
        return TeacherFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related("group")
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filter().form

        return context


class CreateTeachersView(LoginRequiredMixin, CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    form_class = TeacherCreateForm


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    form_class = TeacherCreateForm


class DeleteTeachersView(LoginRequiredMixin, DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
