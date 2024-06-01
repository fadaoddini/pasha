from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import redirect


def check_is_active(user):
    return user.is_active


def check_is_ok(user, pk):
    if user.pk == pk:
        return True
    return False


def check_user_active(user):
    check_info = User.objects.filter(user=user).first()
    if check_info is None:
        return False
    if user.info.is_active is True:
        return True
    return False

