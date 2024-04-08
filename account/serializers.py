from rest_framework import serializers
from .models import Student, Faculty

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name", "id", "department", "email_id", "password"]

        # It hides the password whenever it gets returned
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_email_id(self, attrs):
        return super().validate(attrs)

    # To hash our password 
    def create(self, validated_data):
        password = validated_data.pop("password", None)   # To extract the password from validated data
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ["name", "id", "email_id", "password"]

        # It hides the password whenever it gets returned
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def validate_email_id(self, attrs):
        return super().validate(attrs)

    # To hash our password 
    def create(self, validated_data):
        password = validated_data.pop("password", None)   # To extract the password from validated data
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance