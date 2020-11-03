from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
# from django

#only required if u use get or post method to update quary
from .form import itemForm

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

class ItemDetailView(DetailView):
	model = Item



class ItemCreateView(CreateView):
	model = Item
	fields = ['product', 'product_name', 'label', 'product_price']

	def get_success_url(self):
		return reverse('list-home')

class DeleteItem(DeleteView):
	model = Item
	def get_success_url(self):
		return reverse('list-home')

class ItemUpdateView(UpdateView):
	model = Item
	fields = ['product', 'product_name', 'label', 'product_price']
	def get_success_url(self):
		return reverse('list-home')
		#update item using get and post method
	# template_name = 'compare/item_form.html'
	# success_url = 'list-home'

	# def get(self, request, pk):
	# 	item = get_object_or_404(Item, pk=pk)
	# 	form = itemForm(instance= Item )
	# 	ctx = { 'form':form }
	# 	return render(request, self.template_name, ctx)

	# def post(self, request, pk):
	# 	item = get_object_or_404(Item, pk=pk)
	# 	form = itemForm(request.POST, instance = item)
	# 	if not form.is_valid():
	# 		ctx = { 'form': form }
	# 		return render(request, self.template_name, ctx)
	# 	form.save()
	# 	return redirect(self.success_url)


#searchbar

def search(request):
	if request.method == 'GET':
		search = request.GET.get('search')
		item = Item.objects.all().filter(product='search')
		ctx = {
		'items':item
		}
		return render(request, 'compare/search_list.html', ctx)


