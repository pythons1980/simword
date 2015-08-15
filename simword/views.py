# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView
from django.utils.translation import ugettext_lazy as _

from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import StringListForm
from .models import StringList
from .serializers import StringListSerializer
from .utils import most_similar_word


class StringListCreateView(CreateView):
    model = StringList
    form_class = StringListForm
    template_name = 'simword/stringlist_create.html'

    def form_valid(self, form):
        instance = form.save()
        word = form.cleaned_data.get('word', '')
        params = {'q': word}
        return HttpResponseRedirect(reverse('search', kwargs=params))


class SearchView(DeleteView):
    model = StringList
    template_name = 'simword/search.html'

    def dispatch(self, request, *args, **kwargs):
        """If no q parameter then redirects to string list"""
        self.q = self.kwargs.get('q', None)
        if not self.q:
            return HttpResponseRedirect(reverse('stringlist_input'))
        return super(SearchView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return  StringList.objects.all().order_by('-created_at').first()

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data()
        context['input_word'] = self.q
        # Find most similar word.
        try:
            context['most_similar_word'] = most_similar_word(self.q, self.object.string_list)
        except IndexError:
            context['most_similar_word'] = (0, _('Some error'))
        return context


class SearchRESTView(APIView):

    def get(self, request, *args, **kwargs):
        stringlist_object = StringList.objects.all().order_by('-created_at').first()
        serializer = StringListSerializer(stringlist_object)
        q = self.kwargs.get('q', None)
        response_data = serializer.data
        if q:
            response_data['word'] = q
            # Find most similar word.
            try:
                response_data['similar_word'] = most_similar_word(q, stringlist_object.string_list)[1]
            except IndexError:
                pass
        return Response(response_data)


class StringListRESTView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = StringList.objects.all().order_by('-created_at')
    serializer_class = StringListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
