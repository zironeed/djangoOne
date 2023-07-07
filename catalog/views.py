from django.shortcuts import render
from catalog.models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {
        'product_list': products
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Вам письмо, вот. От {name} ({phone}): \n{message}')
    return render(request, 'catalog/contacts.html')


def product_cart(request, product_id):
    products = Product.objects.get(pk=product_id)
    context = {"id": product_id,
               "name": products.name,
               "price": products.price,
               "description": products.description,
               "image": products.image
               }
    return render(request, 'catalog/product_cart.html', context)
