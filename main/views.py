from django.http.response import HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView
from main.forms import ContactForm
from django.shortcuts import render 
from django.contrib import messages

def error_404(request, exception):
    data = {}
    return render(request, 'main/404.html', data)


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cf_form"] = ContactForm()
        return context
    

class AboutView(TemplateView):
    template_name = 'main/about.html'


class ServicesView(TemplateView):
    template_name = 'main/services.html'


class FaqView(TemplateView):
    template_name = 'main/faq.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            value = form.save()
        messages.add_message(request, messages.SUCCESS, 'We would reply as soon as possible')
        return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cf_form"] = ContactForm()
        return context

    
class PrivacyView(TemplateView):
    template_name = 'main/privacy.html'


class TermsView(TemplateView):
    template_name = 'main/terms.html'
