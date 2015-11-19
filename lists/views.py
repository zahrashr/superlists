from django.core.exceptions import ValidationError
#from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

def home_page(request):
	comments='yey, waktunya berlibur'
		
	return render(request, 'home.html', {'comments': comments})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	error = None
	list_true = Item.objects.filter(list_id=list_id).count()	

	comments = ''

	if list_true==0:
		comments='yey, waktunya berlibur'
	elif list_true<5:
		comments='sibuk tapi santai'
	else:
		comments='oh tidak'
	
	if request.method == 'POST':
		try:
			item = Item.objects.create(text=request.POST['item_text'], list=list_)
			item.full_clean()
			item.save()
			return redirect(list_)
		except ValidationError:
			error = "You can't have an empty list item"

	return render(request, 'list.html', {'list': list_, 'comments': comments, 'error': error})

def new_list(request):
	list_ = List.objects.create()
	item = Item(text=request.POST['item_text'], list=list_)
	try:
		item.full_clean()
		item.save()
	except ValidationError:
		list_.delete()
		error = "You can't have an empty list item"
		return render(request, 'home.html', {"error": error})
	return redirect(list_)


