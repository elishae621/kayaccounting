from django.http.response import HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, View
from django.contrib import messages
from main.models import Subscriber, ContactMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import json
with open(settings.BASE_DIR / 'kay_config.json') as config_json:
    config = json.load(config_json)



class ComingSoonView(TemplateView):
    template_name = 'main/coming_soon.html'


def error_404(request, exception):
    messages.add_message(request, messages.DEBUG, "The page you are looking for does not exist")
    return HttpResponseRedirect('/')


class HomeView(TemplateView):
    template_name = 'main/home.html'

class ContactView(View):
    def get(self, request, *args, **kwargs):
        try:
            Subscriber.objects.create(email=request.GET.get('email'))
            messages.add_message(request, messages.SUCCESS,
                             'We would reply as soon as possible')
        except:
            pass
        return HttpResponseRedirect('/')

class OrderView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        form = request.POST.get('form')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        number = request.POST.get('number')
        service = request.POST.get('service')
        packages = request.POST.get('packages')
        if form == "Bookkeeping":
            text_message = f"Order type:\t{form}\n\nname:\t{name}\n\nemail:\t{email}\n\nphone:\t{phone}"
        elif form == "Payroll support":
            text_message = f"Order type:\t{form}\n\nname:\t{name}\n\nemail:\t{email}\n\nphone:\t{phone}\n\nnumber of employees:\t{number}"
        elif form == "Business support": 
            text_message = f"Order type:\t{form}\n\nname:\t{name}\n\nemail:\t{email}\n\nphone:\t{phone}\n\nspecific service:\t{service}"
        else: 
            text_message = f"Order type:\t{form}\n\nname:\t{name}\n\nemail:\t{email}\n\nphone:\t{phone}\n\nnumber of employees:\t{number}\n\ntraining packages:\t{packages}"
        title = f"{form} order was entered"
        text_message = text_message
        from_email = config['MAIL_USERNAME']
        to_email = config['CLIENT']
        msg = EmailMultiAlternatives(
            title, text_message, from_email, to_email)
        value = msg.send(fail_silently=False)
        messages.add_message(request, messages.SUCCESS, f'Your {form} order has been received we would reply as soon as possible')
        return HttpResponseRedirect('/')


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
        