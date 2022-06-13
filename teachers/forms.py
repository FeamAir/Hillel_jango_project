from django import forms

from django_filters import FilterSet

from .models import Teacher


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'univer_subject',
            'phone_number',
            'age'
        ]

    def clean_phone_number(self):
        str1 = self.cleaned_data["phone_number"]
        f = filter(str.isdecimal, str1)
        result = "".join(f)
        return result


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
