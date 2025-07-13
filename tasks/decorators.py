# decorators.py
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        elif not request.user.is_staff:  # o usar request.user.is_superuser
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view
