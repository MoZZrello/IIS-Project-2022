from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.role.get_role_display() in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Nemáte přístupová práva.')

        return wrapper_func
    return decorator
