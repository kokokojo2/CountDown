from django.core.exceptions import ValidationError
from datetime import datetime


def positive_date_validator(datetime_obj):
    """
    This validator is used to check whether given datetime_obj is in future
    """
    if datetime_obj.replace(tzinfo=None) < datetime.now():
        raise ValidationError('The finish date and time is in the past.')
