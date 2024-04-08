from django.shortcuts import redirect, render
from .forms import ContactForm
from django.core.mail import EmailMessage
import os
from django.core.mail import send_mail

# def Home(request):
#     """
#     Home Page with Contact Form
#     """
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']

#             # Send email
#             message_body = f'''
#             New message:
#             From: {email}
#             Name: {name}
#             Message: {message}
#             '''
#             send_mail(subject, message_body, email, [''])

#             return redirect('success')
#     else:
#         form = ContactForm()

#     context = {'form': form}
#     return render(request, "index.html", context)

def Home(request):
    """
    Home Page with Contact Form
    """
    recipient_email = ''  # Specify recipient email directly

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            subject_line = 'Contact form submission from {}'.format(name)
            
            # Send email
            email_message = EmailMessage(
                subject_line,
                message,
                email,
                [''],  
                reply_to=[email]
            )
            
            result = email_message.send()
            print("Email sending result:", result)
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, "index.html", context)



def success_view(request):
    return render(request, 'success.html')
