from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def login_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        if not target_user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated