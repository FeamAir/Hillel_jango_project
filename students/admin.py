from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
    ]

    list_display_links = list_display
    list_per_page = 5
    search_fields = [
        'first_name',
        'last_name',
    ]

    fields = [
        ('first_name', 'last_name'),
        'age',
        'phone_number'
    ]

    readonly_fields = ['phone_number', 'age']


admin.site.register(Student, StudentAdmin)
