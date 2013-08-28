# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from lists_app.forms import CreateOrderForm, CreateItemForm, UpdateOrderForm
from lists_app.models import Order, Item


def home(req):
    orders = Order.objects.all()
    return render(req, 'list_app/all_orders.html', {'all_orders': orders})


def create_order(req):
    message = None
    if req.POST:
        form = CreateOrderForm(req.POST)
        if form.is_valid():
            form.save()
            message = "Товар добавлен успешно!"
    else:
        form = CreateOrderForm()
    return render(req, 'list_app/create_order.html', {'form': form, 'message': message})


def create_item(req):
    if req.POST:
        form = CreateItemForm(req.POST)
        if form.is_valid():
            form.save()
            redirect_address = req.POST.get('from', '/')
            return HttpResponseRedirect(redirect_address)
    else:
        form = CreateItemForm()
    return render(req, 'list_app/create_item.html', {'form': form})


def update_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    if request.POST:
        form = UpdateOrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home")
    else:
        form = UpdateOrderForm(instance=order)

    return render(request, 'list_app/show_order.html', {'form': form, 'order': order})