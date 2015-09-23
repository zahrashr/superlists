from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
	#if request.method == 'POST':
	#	Item.objects.create(text=request.POST['item_text'])
	#	return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'home.html')
		
	#comments = ''
	
	#if Item.objects.count()==0:
	#	comments='yey, waktunya berlibur'
	#elif Item.objects.count()<5:
	#	comments='sibuk tapi santai'
	#else:
	#	comments='oh tidak'	
	
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})

def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/the-only-list-in-the-world/')
