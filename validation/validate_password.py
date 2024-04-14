import re
from django.core.exceptions import ValidationError


def validate_password(password_value: str):
    password = re.match(
        pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        string=password_value
    )
    if not password:
        raise ValidationError(
            'Password must contain: at least one uppercase letter, one lowercase letter, ' +
            'one number and one special character. ' +
            'Must not contain spaces'
        )