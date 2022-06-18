from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView


from .forms import CourseBaseForm
from .models import Course


class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'
    form_class = CourseBaseForm


class ListCourseView(ListView):
    model = Course
    template_name = "courses/list.html"


class UpdateCourseView(LoginRequiredMixin, UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'
    form_class = CourseBaseForm


class DeleteCourseView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'
