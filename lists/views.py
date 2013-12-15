from django.shortcuts import redirect, render
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    return render(request, 'home.html', {'items': Item.objects.all()})
