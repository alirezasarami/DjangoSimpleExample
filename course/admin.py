from django.contrib import admin
from .models import Course , Departman

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','code' , 'name' , 'department']
    search_fields = ('name' , )
    list_filter = ['department']

class DepartmanAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Course , CourseAdmin)
admin.site.register(Departman , DepartmanAdmin)
