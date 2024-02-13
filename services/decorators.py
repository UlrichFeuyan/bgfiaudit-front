from functools import wraps
from django.http import JsonResponse

def login_required_api(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Vérifier la présence du token d'accès dans la session
        access_token = request.session.get('access_token')
        if not access_token:
            # Rediriger ou renvoyer une réponse d'erreur selon vos besoins
            return JsonResponse({'error': 'L\'utilisateur n\'est pas connecté'}, status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view