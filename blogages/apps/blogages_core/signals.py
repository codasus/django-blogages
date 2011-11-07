from django.contrib.auth.models import User
from django.dispatch import receiver

from userena.signals import signup_complete


@receiver(signup_complete)
def set_admin_if_first(user, **kwargs):
    if User.objects.filter(is_staff=True).count() == 0:
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
