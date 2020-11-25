""" These are  View tests """
from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    """ a test for Item Views  """
    def test_get_todo_list(self):
        """ test_get_todo_list  """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo_list.html")

    def test_get_add_item_page(self):
        """ Test Add Item  """
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/add_item.html")

    def test_get_edit_item_page(self):
        """ Test Get Item  """
        item = Item.objects.create(name="Test Todo Item")
        # f string is a basic formatter
        response = self.client.get(f"/edit/{item.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/edit_item.html")

    def test_can_add_item(self):
        """ Test Item Add  """
        response = self.client.post("/add", {"name": "Test Added Item"})
        self.assertRedirects(response, "/")

    def test_can_delete_item(self):
        """ Test Item Delete  """
        testitem = Item.objects.create(name="Test Todo Item")
        # f string is a basic formatter
        response = self.client.get(f"/delete/{testitem.id}")
        self.assertRedirects(response, "/")
        existing_items = Item.objects.filter(id=testitem.id)
        self.assertEqual(len(existing_items), 0)


    def test_can_toggle_item(self):
        """ Test Item Toggle  """
        testitem = Item.objects.create(name="Test Todo Item", done=True)
        # f string is a basic formatter
        response = self.client.get(f"/toggle/{testitem.id}")
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=testitem.id)
        self.assertFalse(updated_item.done)
        updated_item.delete()

    def test_can_edit_item(self):
        """ Test Item Toggle  """
        item = Item.objects.create(name="Test Todo Item")
        response = self.client.post(f"/edit/{item.id}", {"name": "Updated Name"})
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, "Updated Name")
