""" These are Model tests """
from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    """ a test for Models  """
    def test_done_defaults_to_false(self):
        """ Make sure default is false  """
        item = Item.objects.create(name="Test todo Item")
        self.assertFalse(item.done)

    def test_test_item_string_method_returns_name(self):
        """ Make sure name is returned not object id  """
        item = Item.objects.create(name="test todo Item")
        self.assertEqual(str(item), "test todo Item")
