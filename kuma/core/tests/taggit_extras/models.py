from __future__ import absolute_import
from django.db import models

from ...managers import NamespacedTaggableManager


class Food(models.Model):
    name = models.CharField(max_length=50)
    tags = NamespacedTaggableManager()
