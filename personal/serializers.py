from rest_framework import serializers
from .models import Department, Personal

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class PersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personal
        fields = '__all__'

# ------------------------ NESTED SERIALIZER ----------------------- #
class DepartmentPersonalNestedSerializer(serializers.ModelSerializer):

    personal = PersonalSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'personal')
    