""" This is a docstring  """
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def get_todo_list(request):
    """ Describe me """
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "todo/todo_list.html", context)

def add_item(request):
    """ Describe me """
    if request.method == "POST":
        form = ItemForm(request.POST)   # Get form data
        if form.is_valid():   # does all field / model alignment checking
            form.save()
        return redirect("get_todo_list")

    form = ItemForm()
    context = {
        "form": form
    }

    return render(request, "todo/add_item.html", context)
