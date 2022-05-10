from django.db import models

from faker import Faker
from random import choice as ch


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    univer_subject = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.univer_subject} {self.age}'

    @staticmethod
    def gen_teachers(cnt):
        fk = Faker()
        test_list = ["Mathematics", "Chemistry", "Algebra", "Logic", "History",
                     "Physics"]
        for _ in range(cnt):
            tc = Teacher(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                univer_subject=ch(test_list),
                age=fk.random_int(min=25, max=55))
            tc.save()