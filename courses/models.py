from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=30)
    hour = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name
