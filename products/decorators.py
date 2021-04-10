from django.http import HttpResponse
from django.shortcuts import redirect

def unathenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


def allowed_users(allowed_users=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_users:
                return view_func(request, *args, **kwargs)
            else:
                # return HttpResponse("Error")
                return redirect('userprofile')

        return wrapper
    return decorator


def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        print("Group: ",group)

        if group == 'admin':
            return view_func(request, *args, **kwargs)

        if group == 'guest':
            # return HttpResponse("Error")
            return redirect('userprofile')

    return wrapper


