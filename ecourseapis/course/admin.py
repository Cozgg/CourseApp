from django.contrib import admin
from django.utils.safestring import mark_safe

from course.models import Category, Courses

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description', 'created_date', 'active']
    list_filter = ['subject', 'created_date']
    search_fields = ['subject']
    readonly_fields = ['image_view']

    def image_view(self, course):
        if course.image:
            return mark_safe(f'<img src ="/static/{course.image.name}" width = "200" />')



admin.site.register(Category)
admin.site.register(Courses, CourseAdmin)

