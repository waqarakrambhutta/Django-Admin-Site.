from django.shortcuts import render
from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()
    print(query_set)
    return render(request, 'hello.html', {'name': 'Mosh','results':list(query_set)})
