from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm


def category_list(request):
    categories = Category.objects.all()
    search = request.GET.get('query')
    if search:
        categories = categories.filter(name__icontains=search)
    ctx = {'categories':categories}
    return render(request, 'categories/list.html', ctx)

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = Category(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                icon=form.cleaned_data['icon']
            )
            category.save()
            return redirect('categories:list')
    else:
        form = CategoryForm()
    ctx = {'form': form}
    return render(request, 'categories/form.html', ctx)


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.description = form.cleaned_data['description']
            category.icon = form.cleaned_data['icon']
            category.save()
            return redirect('categories:list')
    else:
        form = CategoryForm(initial={
            'name': category.name,
            'description': category.description,
            'icon': category.icon
        })
    ctx = {'form': form, 'category': category}
    return render(request, 'categories/form.html', ctx)

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    ctx = {'category':category}
    return render(request, 'categories/detail.html', ctx)

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:list')
    ctx = {'category':category}
    return render(request, 'categories/delete-confirm.html', ctx)