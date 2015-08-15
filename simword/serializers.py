# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import StringList
from .fields import JSONSerializerField

class StringListSerializer(serializers.ModelSerializer):

    string_list = JSONSerializerField()

    class Meta:
        model = StringList
        fields = ('string_list',)
