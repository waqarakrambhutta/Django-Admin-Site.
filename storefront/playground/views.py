from django.shortcuts import render
from store.models import Product


def say_hello(request):
    query_set = Product.objects.filter(collection__title__icontains='b')
    
    return render(request, 'hello.html', {'name': 'Mosh','results':query_set})
    # return render(request, 'hello.html', {'name': 'Mosh','results':list(query_set)})

