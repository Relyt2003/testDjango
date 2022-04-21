from django.shortcuts import render
from testytest.models import Product

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

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #
    # }
    context = {
        'object': obj
    }

    return render(request, "testytest/product/detail.html", context)