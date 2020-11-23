""" This is the models we use """
from django.db import models


class Item(models.Model):
    """ Describe me """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        """ override model default - return the name. """
        return self.name
