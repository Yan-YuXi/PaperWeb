from django.utils import timezone

def utcnow():
    return timezone.now().replace(tzinfo=timezone.utc)