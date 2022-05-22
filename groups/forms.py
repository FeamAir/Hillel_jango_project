from django import forms

from .models import Group


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            "language_groups",
            "univer_subject",
            "cnt_students",
            "phone_number"
        ]

    def clean_phone_number(self):
        str1 = self.cleaned_data["phone_number"]
        f = filter(str.isdecimal, str1)
        result = "".join(f)
        return result
