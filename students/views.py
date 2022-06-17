from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

from .forms import StudentBaseForm
from .models import Student


def generate_students(request):
    Student.gen_students()
    return HttpResponseRedirect(reverse('students:list'))


class ListStudentsView(ListView):
    model = Student
    template_name = "students/list.html"


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
    form_class = StudentBaseForm


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'
    form_class = StudentBaseForm


class DeleteStudentsView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    template_name = 'students/delete.html'
