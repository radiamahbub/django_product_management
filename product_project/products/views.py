from django.shortcuts import render, redirect
from products.models import *

def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        production_date = request.POST.get('production_date')
        image = request.FILES.get('image')
        product_type = request.POST.get('product_type')
        

        ProductModel.objects.create(
            name = name,
            description = description,
            price = price,
            production_date = production_date,
            image = image,
            product_type = product_type
        )

        return redirect('product_list')

    return render(request, 'add-product.html')

def product_list(request):

    product_data = ProductModel.objects.all()

    filtered_data = ProductModel.objects.filter(price__gt = 900)
    keyboard_data = ProductModel.objects.filter(name = "keyboard")
    mouse_data = ProductModel.objects.filter(name = "Mouse")

    context = {
        'product_data':product_data,
        'filtered_data': filtered_data,
        'keyboard_data': keyboard_data,
        'mouse_data':mouse_data,
    }

    return render(request, 'product-list.html', context)

def delete_product(request, p_id):
    ProductModel.objects.get(id = p_id).delete()
    return redirect('product_list')

def update_product(request, p_id):
    product_data = ProductModel.objects.get(id = p_id)

    if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            production_date = request.POST.get('production_date')
            image = request.FILES.get('image')
            product_type = request.POST.get('product_type')

            product_data.name = name
            product_data.description = description
            product_data.price = price
            product_data.production_date = production_date
            product_data.product_type = product_type

            if image:
                product_data.image = image

            product_data.save()
            
            return redirect('product_list')

    context = {
        'product_data':product_data
    }

    return render(request, 'update_product.html', context)










# from django.utils.dateparse import parse_datetime
# production_date = parse_datetime(production_date)

# Create your views here.