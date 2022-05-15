from django.db import models
from .validators import phone_number_validator


class Group(models.Model):
    language_groups = models.CharField(max_length=50)
    univer_subject = models.CharField(max_length=50)
    cnt_students = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15, null=True, validators=[phone_number_validator])

    def __str__(self):
        return f'{self.language_groups} {self.univer_subject} {self.cnt_students}-{self.phone_number}'
