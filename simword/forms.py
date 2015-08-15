# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import StringList


class StringListForm(forms.ModelForm):
    word = forms.CharField(label=_('Word'), required=True)
    input_strings = forms.CharField(label=_('Strings'), widget=forms.Textarea(), required=False)
    input_file = forms.FileField(label=_('File of strings'), required=False)

    class Meta:
        model = StringList
        fields = ('word', 'input_file', 'input_strings',)

    def clean(self):
        cleaned_data = super(StringListForm, self).clean()
        input_strings = cleaned_data.get('input_strings', None)
        input_file = cleaned_data.get('input_file', None)
        if not input_strings and not input_file:
            raise forms.ValidationError(_('Fill one of the folowing fields: "Strings", "File of strings"'))
        return cleaned_data

    def save(self, commit=True):
        instance = super(StringListForm, self).save(commit=False)
        string_list = []

        # Add strings from text field.
        input_strings = self.cleaned_data.get('input_strings', None)
        if input_strings:
            string_list += input_strings.split(',')

        # Add strings from file.
        input_file = self.files.get('input_file', None)
        if input_file:
            string_list += input_file.read().split(',')

        instance.string_list = string_list
        instance.save()
        return instance
