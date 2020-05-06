
from django.views.generic.list import ListView

from items.models import Item


class HomePageView(ListView):
    model = Item
    template_name = 'items/home.html'
