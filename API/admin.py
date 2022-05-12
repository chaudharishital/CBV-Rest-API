from django.contrib import admin
from API.models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','ename','esal','eaddress']
