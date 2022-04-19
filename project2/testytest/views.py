from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'testytest/home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'testytest/contact.html', {})


def about_view(request, *args, **kwargs):
    return render(request, 'testytest/about.html', {})


# def home_view(request, *args, **kwargs):
#     return render(request, 'home.html', {})