from django import forms
from kayaccounting.utils.forms import MyBaseModelForm
from main.models import ContactMessage


class ContactForm(MyBaseModelForm):
    name = forms.CharField(label=None, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), required=True)
    email = forms.EmailField(label=None, widget=forms.EmailInput(attrs={'placeholder': 'Your emaii address'}), required=True)
    phone = forms.CharField(label=None, widget=forms.TextInput(attrs={'placeholder': 'Your phone number'}), required=True)
    content = forms.CharField(label=None, widget=forms.Textarea(attrs={'placeholder': 'Say whatever you want.'}), required=True)

    class Meta:
        model = ContactMessage 
        fields = ('name', 'email', 'phone', 'content')