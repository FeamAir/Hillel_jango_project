from django.contrib import admin

from groups.models import Group

from teachers.models import Teacher


class TeacherInlineTable(admin.TabularInline):
    model = Teacher
    fields = [
        "first_name",
        "last_name",
        "univer_subject",
        "phone_number",
    ]

    extra = 0

    readonly_fields = [
        "first_name",
        "last_name",
    ]


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'start_date',
        'end_date',
        'course_group',
    ]

    list_display_links = list_display
    list_per_page = 5
    search_fields = [
        'name',
        'course_group',
    ]

    fields = [
        "name",
        ('start_date', 'end_date'),
        'course_group',
        ('create_datetime', 'update_datetime')
    ]

    readonly_fields = ['create_datetime', 'update_datetime']

    inlines = [TeacherInlineTable]


admin.site.register(Group, GroupAdmin)
