from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class ThankYouView(TemplateView):
    template_name = 'pages/verify_email.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
