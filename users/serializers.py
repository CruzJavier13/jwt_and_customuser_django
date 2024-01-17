from rest_framework import serializers
from .models import User

class user_register_serializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    password2=serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model=User
        fields=["email", "first_name", "last_name", "password", "password2"]

    def validate(self, attr):
        password=attr.get('password', '')
        password2=attr.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("password do not match")
        return attr

    def create(self, validated_data):
        user=User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data.get('password'),
        )
        return user