from django.shortcuts import render
from .models import Item
from django.views.generic import ListView

# Create your views here.
def home(request):
	ctx = {
	'items':Item.objects.all()
	}
	return render(request, 'compare/list_view.html', ctx)


class ItemListView(ListView):
	model = Item
	template_name = 'compare/list_view.html'
	context_object_name='items'