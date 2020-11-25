""" These are Model tests """
from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    """ a test for TestItemForm  """
    def test_item_name_is_required(self):
        """ a test for TestItemForm  """
        form = ItemForm({"name": ""}) # not valid
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        #REALLY determine the error
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_done_field_is_not_required(self):
        """ done is not required """
        form = ItemForm({"name": "test Todo"})
        self.assertTrue(form.is_valid())


    def test_field_are_explicit_in_form_metaclass(self):
        """ a test for TestItemForm  """
        # make sure all model fields are known (one could be added or removed)
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ["name", "done"])
