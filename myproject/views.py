from django.shortcuts import redirect, render
from .forms import ContactForm

def Home(request):
    """
    Home Page
    """
    return render(request, "index.html")


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)



def success_view(request):
    return render(request, 'success.html')

