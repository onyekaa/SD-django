# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=50)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
