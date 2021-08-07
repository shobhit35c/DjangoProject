from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect




# Create your views here.

def home(request):



    if request.method == 'POST':

        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ("Added to List!"))
            return render(request,'home.html', {"all_items": all_items})

        if render(request):
            asdf = 2


    else:

        all_items = List.objects.all
        return render(request,'home.html', {"all_items": all_items})


def about(request):
    my_name = "Shobhit Choudhury"

    middle_name = "Choudhury"

    context = {'name': my_name, 'middle': middle_name}

    return render(request, 'about.html', context)


def delete(request, list_id):

    item = List.objects.get(pk= list_id)
    item.delete()
    messages.success(request, ("item deleted!"))
    return redirect('home')

def cross_off(request, list_id):

    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def un_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')



