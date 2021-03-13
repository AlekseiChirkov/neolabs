from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, DetailView, FormView

from apps.landing.models import Content
from apps.landing.forms import PostForm


# class IndexPageView(TemplateView):
#     template_name = 'landing/index.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['contents'] = Content.objects.all()
#         return context


class PostFormView(FormView):
    form_class = PostForm
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contents'] = Content.objects.all()
        return context

    def form_valid(self, form):
        title = form.cleaned_data['title']
        print(title)
        response = {'success': 'Successfully created post'}
        return JsonResponse(response, status=200)

    def form_invalid(self, form):
        response = {'error': 'Error'}
        return JsonResponse(response, status=400)

