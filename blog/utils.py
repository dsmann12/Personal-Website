from django.utils import timezone

def now():
    """
        Helper method for better isolating and testing default datetime values
        for Django models using django.utils.timezone.now()
    """
    # It is difficult to isolate and mock the default values for a Django model
    # The easiest way that helps mitigate issues with patching the fields'
    # default value is wrapping the call to timezone.now around a utility
    # function
    return timezone.now()