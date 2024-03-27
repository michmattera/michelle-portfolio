from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'style': 'width: 100%; height: 40px;'}),
            'email': EmailInput(attrs={'class': 'form-control', 'style': 'width: 100%; height: 40px;'}),
            'subject': TextInput(attrs={'class': 'form-control', 'style': 'width: 100%; height: 40px;'}),
            'message': Textarea(attrs={'class': 'form-control', 'style': 'width: 100%; height: 200px; resize: vertical;'}),
        }