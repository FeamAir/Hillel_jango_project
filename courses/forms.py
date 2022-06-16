from django import forms

from .models import Course


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            "name",
            "hour",
        ]
