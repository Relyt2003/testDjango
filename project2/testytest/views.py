from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'testytest/home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'testytest/contact.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        'my_text': "I'm Anton",
        "my_number": 123,
        "my_list": [100, 12, 34, 34, 100]
    }
    return render(request, 'testytest/about.html', my_context)


# def home_view(request, *args, **kwargs):
#     return render(request, 'home.html', {})