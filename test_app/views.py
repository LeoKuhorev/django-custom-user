from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'test_app/home.html'