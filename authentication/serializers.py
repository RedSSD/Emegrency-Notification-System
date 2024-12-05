from collections import defaultdict

from django.core.exceptions import ValidationError
from djoser.serializers import (
    UserCreatePasswordRetypeSerializer,
    UserSerializer,
    TokenCreateSerializer,
)

from rest_framework import serializers

from .models import CustomUser

from validation.validate_password import validate_password
from validation.validate_phone_number import validate_phone_number


class UserRegistrationSerializer(UserCreatePasswordRetypeSerializer):
    email = serializers.EmailField(
        write_only=True,
    )
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )

    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        model = CustomUser
        fields = ("email", "phone_number", "password", "fullname")

    def validate(self, value):
        custom_errors = defaultdict(list)
        email = value.get('email').lower()
        phone_number = value.get('phone_number').lower()
        password = value.get('password')
        re_password = value.pop('re_password')

        print(re_password)

        if CustomUser.objects.filter(email=email).exists():
            custom_errors['email'].append('Email already registered')
        else:
            value['email'] = email

        if re_password != password:
            custom_errors['password'].append('Passwords do not match')

        try:
            validate_password(password)
        except ValidationError as error:
            custom_errors['password'].append(error.message)

        try:
            validate_phone_number(phone_number)
        except ValidationError:
            custom_errors['phone_number'].append('Phone number is incorrect')

        if custom_errors:
            raise ValidationError(custom_errors)
        else:
            return value
