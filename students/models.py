from django.db import models

from faker import Faker

from .validators import phone_number_validator


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(
        max_length=15,
        null=True,
        validators=[phone_number_validator])

    class Meta:
        db_table = 'student'

    def __str__(self):
        return f'{self.first_name}' \
               f' {self.last_name} ' \
               f'{self.age}-' \
               f'{self.phone_number}'

    @staticmethod
    def gen_students():
        cnt = 10
        fk = Faker()
        for _ in range(cnt):
            tc = Student(
                first_name=fk.first_name(),
                last_name=fk.last_name(),
                age=fk.random_int(min=25, max=55),
                phone_number=fk.phone_number())

            tc.save()
