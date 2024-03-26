from django.shortcuts import redirect, render
from .forms import ContactForm

def Home(request):
    """
    Home Page with Contact Form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, "index.html", context)



def success_view(request):
    return render(request, 'success.html')

