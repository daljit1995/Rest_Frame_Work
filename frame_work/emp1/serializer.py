from rest_framework import serializers
from .models import student
class StudentSerial(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    roll=serializers.IntegerField()
    email=serializers.EmailField()

    def create(self, validated_data):
        return student.objects.create(**validated_data)

    def update(self,instance,validate_data):
        # instance - it is a object from database
        # validate_data - it is comes from 3rd party application
        instance.name=validate_data.get('name',instance.name)
        instance.roll=validate_data.get('roll',instance.roll)
        instance.email=validate_data.get('email',instance.email)
        instance.save()
        return instance