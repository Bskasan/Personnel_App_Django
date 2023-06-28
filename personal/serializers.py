from rest_framework import serializers
from .models import Department, Personal

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class PersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personal
        fields = (
            'first_name',
            'last_name',
            'title'
            )

# ------------------------ NESTED SERIALIZER ----------------------- #
# to see our personal details inside of the each department.
class DepartmentPersonalNestedSerializer(serializers.ModelSerializer):

    personal = PersonalSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'personal')
    