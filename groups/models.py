import datetime

from courses.models import Course

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    course_group = models.OneToOneField(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="course_group"

    )

    class Meta:
        db_table = 'group'

    def __str__(self):
        return self.name
