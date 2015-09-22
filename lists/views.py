from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/')
		
	comments = ''
	
	if Item.objects.count()==0:
		comments='yey, waktunya berlibur'
	elif Item.objects.count()<5:
		comments='sibuk tapi santai'
	else:
		comments='oh tidak'	
	
	items = Item.objects.all()
	return render(request, 'home.html', {'items': items, 'comments': comments})
