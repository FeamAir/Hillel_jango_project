# Generated by Django 4.0.4 on 2022-06-17 06:50

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=15, null=True, validators=[students.validators.phone_number_validator])),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]