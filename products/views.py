from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from categories.models import Category
from orders.models import Order
from .forms import ProductForm


def home(request):
    orders = Order.objects.order_by('-date')[:3]
    ctx = {'orders':orders}
    return render(request, 'index.html', ctx)

def products_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    sort_order = request.GET.get('sort')
    search = request.GET.get('query')
    if category_id:
        category_id = int(category_id)
        products = products.filter(category__id=category_id)
    if sort_order == 'low_to_high':
        products = products.order_by('price')
    elif sort_order == 'high_to_low':
        products = products.order_by('-price')
    if search:
        products = products.filter(name__icontains=search)
    ctx = {
        'products': products,
        'categories':categories,
    }
    return render(request, 'products/list.html', ctx)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image'],
            )
            product.save()
            return redirect( 'products:list')
    form = ProductForm()
    ctx = {'form': form}
    return render(request, 'products/form.html', ctx)

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name=form.cleaned_data['name'],
            product.category=form.cleaned_data['category'],
            product.price=form.cleaned_data['price'],
            product.description=form.cleaned_data['description'],
            product.image=form.cleaned_data['image']
            product.save()
            return redirect( 'products:list')
    form = ProductForm(initial={
        'name':product.name,
        'category':product.category,
        'price':product.price,
        'description':product.description,
        'image':product.image
    })
    ctx = {'form': form, 'product':product}
    return render(request, 'products/form.html', ctx)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product':product}
    return render(request, 'products/detail.html', ctx)

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:list')
    ctx = {'product':product}
    return render(request, 'products/delete-confirm.html', ctx)