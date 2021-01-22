from django.forms import ModelForm

from shop.models import Shop


class ShopCreateForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'image', 'notice', 'info', 'address']
