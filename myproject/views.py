from django.shortcuts import redirect, render

def Home(request):
    """
    Home Page
    """
    return render(request, "index.html")
