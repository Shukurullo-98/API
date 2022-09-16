from .models import User
from rest_framework import serializers, status
from rest_framework.validators import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=40, allow_blank=True)
    email = serializers.EmailField(max_length=80, allow_blank=False)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']

    def validate(self, attrs):
        email = User.objects.filter(email=attrs.get('email')).exists()

        if email:
            raise ValidationError(detail="User with email exists", code=status.HTTP_403_FORBIDDEN)

        username = User.objects.filter(username=attrs.get('username')).exists()

        if username:
            raise ValidationError(detail="User with username exists", code=status.HTTP_403_FORBIDDEN)

        phone_number = User.objects.filter(phone_number=attrs.get('phone_number')).exists()

        if phone_number:
            raise ValidationError(detail="User with username exists", code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_nuber=validated_data['phone_number']
            )
        user.set_password(validated_data['password'])
        user.save()
        return user