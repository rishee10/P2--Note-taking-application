from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from mynote.models import Contact
from .models import Contact
from .forms import ItemForm

# Create your views here.





def object_edit(request, item_id):
    item = Contact.objects.get(pk=item_id)
    form = ItemForm(request.POST, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    # if request.method == 'POST':
    #     form = ItemForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('about1')
    # else:
    #     form = ItemForm(instance=item)
    
    return render(request, 'index.html', {'item': item})

def index1(request,item_id):
    return redirect('index')

def index(request):
    if request.method=="POST":
        name1=request.POST.get("name1")
        name=request.POST.get("name")
        
        contact=Contact(name=name, name1=name1)
        contact.save()
    
    

    # return HttpResponse("this is home page")

    
    return render(request,"index.html")




def about(request, item_id):
    item = get_object_or_404(Contact, pk=item_id)
    return render(request, 'about.html', {'item': item})




def about1(request):
    items=Contact.objects.all()
    return render(request, "about1.html", {"items":items})

    

def contact(request):
    return HttpResponse("This is contact")



def delete_object(request, item_id):
    item = get_object_or_404(Contact, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('about1')
    return redirect('about1')

def stosaved(request, item_id):
    return redirect('about1')



# def update(request, item_id):
#     up=Contact.objects.get(pk=item_id)
    
#     if request.method=="POST":
#         contact.save()
#     return redirect('about1')

def edit(request, item_id):
    item=Contact.objects.get(pk=item_id)
    return render(request, "edit.html", {'item':item})


def seetoabout1(request):
    return redirect('about1')

def seetoindex(request):
    return redirect('index')