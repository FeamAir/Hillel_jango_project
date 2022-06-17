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

    def get_queryset(self):
        teachers_filter = TeacherFilterForm(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related("group")
        )

        return teachers_filter


class CreateTeachersView(CreateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    form_class = TeacherCreateForm


class UpdateTeacherView(UpdateView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/update.html'
    form_class = TeacherCreateForm


class DeleteTeachersView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    template_name = 'teachers/delete.html'
