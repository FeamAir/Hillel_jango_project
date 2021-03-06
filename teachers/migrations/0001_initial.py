# Generated by Django 4.0.4 on 2022-05-30 14:23

from django.db import migrations, models
import django.db.models.deletion
import teachers.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('univer_subject', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=15, null=True, validators=[teachers.validators.phone_number_validator])),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teachers', to='groups.group')),
            ],
        ),
    ]
