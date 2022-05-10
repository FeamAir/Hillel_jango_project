from django.db import models


class Group(models.Model):
    language_groups = models.CharField(max_length=50)
    univer_subject = models.CharField(max_length=50)
    cnt_students = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.language_groups} {self.univer_subject} {self.cnt_students}'
