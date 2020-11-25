""" This is a docstring  """
from django.shortcuts import render, redirect, get_object_or_404
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


def edit_item(request, item_id):
    """ Edit an item  """
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)   # Get form data
        if form.is_valid():   # does all field / model alignment checking
            form.save()
        return redirect("get_todo_list")

    # get an instance of the form, prepopulate it with object instance
    form = ItemForm(instance=item)
    context = {
        "form": form
    }

    return render(request, "todo/edit_item.html", context)


def toggle_item(request, item_id):
    """ Toggle the done status """
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done  # logical not to toggle
    item.save()
    return redirect("get_todo_list")


def delete_item(request, item_id):
    """ Delete the item  """
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect("get_todo_list")
