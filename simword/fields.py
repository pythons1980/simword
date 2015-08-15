# -*- coding: utf-8 -*-
from rest_framework import serializers


class JSONSerializerField(serializers.Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value
