from django.forms.models import ModelForm
from lists_app.models import Order, Item

__author__ = 'logart'


class CreateOrderForm(ModelForm):
    class Meta:
        model = Order

class UpdateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'done']

class CreateItemForm(ModelForm):
    class Meta:
        model = Item