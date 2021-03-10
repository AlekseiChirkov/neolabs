from apps.landing.models import Logo


def globals(request):
    context = {
        'logos': Logo.objects.all()
    }
    return context
