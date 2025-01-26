from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Customer, OrderItem
from .forms import OrderForm, CustomerForm, OrderItemForm


def order_list(request):
    orders = Order.objects.all()
    search = request.GET.get('query')
    if search:
        orders = orders.filter(customer__name__icontains=search)
    ctx = {'orders': orders}
    return render(request, 'orders/list.html', ctx)

def edit_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    customer = order.customer
    order_items = order.items.all()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        customer_form = CustomerForm(request.POST)
        order_item_forms = [OrderItemForm(request.POST, prefix=str(i)) for i in range(len(order_items))]

        if order_form.is_valid() and customer_form.is_valid() and all([form.is_valid() for form in order_item_forms]):
            order.status = order_form.cleaned_data['status']
            order.date = order_form.cleaned_data['date']
            order.save()

            customer.name = customer_form.cleaned_data['name']
            customer.email = customer_form.cleaned_data['email']
            customer.phone = customer_form.cleaned_data['phone']
            customer.address = customer_form.cleaned_data['address']
            customer.save()

            for i, form in enumerate(order_item_forms):
                item = order_items[i]
                if form.is_valid():
                    item.product = form.cleaned_data['product']
                    item.quantity = form.cleaned_data['quantity']
                    item.price = form.cleaned_data['price']
                    item.save()

            return redirect('orders:list')
    else:
        order_form = OrderForm(initial={
            'order_id': f'#{order.id}',
            'date': order.date,
            'status': order.status,
        })
        customer_form = CustomerForm(initial={
            'name': customer.name,
            'email': customer.email,
            'phone': customer.phone,
            'address': customer.address,
        })
        order_item_forms = [
            OrderItemForm(initial={
                'product_name': item.product.name,
                'quantity': item.quantity,
                'price': item.price,
                'total': item.total_price(),
            }, prefix=str(i)) for i, item in enumerate(order_items)
        ]

    ctx = {
        'order_form': order_form,
        'customer_form': customer_form,
        'order_item_forms': order_item_forms,
    }

    return render(request, 'orders/form.html', ctx)

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = order.items.all()
    ctx = {
        'order':order,
        'order_items':order_items
    }
    return render(request, 'orders/detail.html', ctx)


def delete_order_item(request, pk):
    item = get_object_or_404(OrderItem, pk=pk)
    order = item.order
    item.delete()
    order.total = order.calculate_total()
    order.save()
    return redirect('orders:detail')