# Generated by Django 4.0.4 on 2022-05-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_rename_teacher_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
