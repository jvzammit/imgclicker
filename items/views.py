
from django.views.generic.list import ListView

from items.models import Item


class HomePageView(ListView):
    model = Item
    template_name = 'items/home.html'

    def get_context_data(self, **kwargs):
        """Just to add ipdb breakpoint for demo purposes"""
        context = super().get_context_data(**kwargs)
        import ipdb; ipdb.set_trace()
        return context
