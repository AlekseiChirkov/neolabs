from django.views.generic import TemplateView

from apps.landing.models import Content


class IndexPageView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contents'] = Content.objects.all()
        return context



