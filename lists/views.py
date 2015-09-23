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
	
	comments = ''

	if Item.objects.count()==0:
		comments='yey, waktunya berlibur'
	elif Item.objects.count()<5:
		comments='sibuk tapi santai'
	else:
		comments='oh tidak'
	return render(request, 'list.html', {'list': list_, 'comments': comments})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))
