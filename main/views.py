from django.http.response import HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, View
from django.contrib import messages
from main.models import Subscriber, ContactMessage



class ComingSoonView(TemplateView):
    template_name = 'main/coming_soon.html'


def error_404(request, exception):
    messages.add_message(request, messages.DEBUG, "The page you are looking for does not exist")
    return HttpResponseRedirect('/')


class HomeView(TemplateView):
    template_name = 'main/home.html'



class AboutView(TemplateView):
    template_name = 'main/about.html'


class ServicesView(TemplateView):
    template_name = 'main/services.html'


class FaqView(TemplateView):
    template_name = 'main/faq.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get(self, request, *args, **kwargs):
        try:
            Subscriber.objects.create(email=request.GET.get('email'))
            messages.add_message(request, messages.SUCCESS,
                             'We would reply as soon as possible')
        except:
            pass
        return HttpResponseRedirect('/')

class PrivacyView(TemplateView):
    template_name = 'main/privacy.html'


class TermsView(TemplateView):
    template_name = 'main/terms.html'



class ChatView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        contactMessage = ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return JsonResponse({
                'ok': True,
                'message': "Your message has been received, we would apply by email as soon as possible"
            })
        