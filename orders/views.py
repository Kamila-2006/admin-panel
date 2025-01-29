from django.shortcuts import render, get_object_or_404, redirect
from .models import Order


def order_list(request):
    orders = Order.objects.all()
    search = request.GET.get('query')
    status = request.GET.get('status')
    if search:
        orders = orders.filter(customer__name__icontains=search)
    if status:
        orders = orders.filter(status=status)
    ctx = {'orders': orders}
    return render(request, 'orders/list.html', ctx)


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = order.items.all()
    ctx = {
        'order':order,
        'order_items':order_items
    }
    return render(request, 'orders/detail.html', ctx)
