from django.contrib import admin

# Register your models here.
from .models import Student
class Studentadmin(admin.ModelAdmin):
    list_display=["id","name","marks"]
admin.site.register(Student,Studentadmin)