from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'univer_subject',
        'age',
        'phone_number',
        'group',
    ]

    list_display_links = list_display
    list_per_page = 5
    search_fields = [
        'first_name',
        'last_name',
        'group',
    ]

    fields = [
        ('first_name', 'last_name', 'age'),
        'univer_subject',
        'phone_number',
        'group',

    ]

    readonly_fields = ['univer_subject']


admin.site.register(Teacher, TeacherAdmin)
