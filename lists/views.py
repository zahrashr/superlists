from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
	#if request.method == 'POST':
	#	Item.objects.create(text=request.POST['item_text'])
	#	return redirect('/lists/the-only-list-in-the-world/')
	#return render(request, 'home.html')
		
	comments='yey, waktunya berlibur'
		
	
	#items = Item.objects.all()
	return render(request, 'home.html', {'comments': comments})

def view_list(request, list_id):
	#items = Item.objects.all()
	list_ = List.objects.get(id=list_id)
	list_true = Item.objects.filter(list_id=list_id).count()	

	comments = ''

	if list_true==0:
		comments='yey, waktunya berlibur'
	elif list_true<5:
		comments='sibuk tapi santai'
	else:
		comments='oh tidak'
	return render(request, 'list.html', {'list': list_, 'comments': comments})

def new_list(request):
	list_ = List.objects.create()
	item = Item(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
