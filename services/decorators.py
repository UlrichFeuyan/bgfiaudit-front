from functools import wraps
from django.http import JsonResponse
from django.shortcuts import redirect


def login_required_api(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Vérifier la présence du token d'accès dans la session
        access_token = request.session.get('token')
        if not access_token:
            # Rediriger ou renvoyer une réponse d'erreur selon vos besoins
            return redirect('services:signIn')
        return view_func(request, *args, **kwargs)
    return _wrapped_view