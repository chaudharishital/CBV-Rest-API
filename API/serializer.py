from rest_framework import serializers
from .models import Employee
class EmployeeSerializer(serializers.Serializer):
    ename=serializers.CharField(max_length=50)
    esal=serializers.IntegerField()
    eaddress=serializers.CharField(max_length=50)
    def create(self,data):
        return Employee.objects.create(**data)
    def validate_ename(self,value):
        if len(value)<4:
            raise serializers.ValidationError("name length should be >4")
        return value
