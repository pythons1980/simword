# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from picklefield.fields import PickledObjectField


class StringList(models.Model):
    """Stores latest list of strings.
    """
    string_list = PickledObjectField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, db_index=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, null=True, db_index=True, verbose_name=_('Updated at'))
