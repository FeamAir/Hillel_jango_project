from django import forms

from .models import Student


class StudentBaseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        exclude = ['age']
