import re
from django.core.exceptions import ValidationError


def validate_phone_number(phone_number_value: str):
    phone_number = re.match(r'^\+(?:[0-9]●?){6,14}[0-9]$', phone_number_value)
    if not phone_number:
        raise ValidationError(
            f'Invalid phone number: {phone_number_value}'
        )
