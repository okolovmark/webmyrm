# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import TrashSetting
from django.shortcuts import render


class IndexView(generic.ListView):
    template_name = 'trash/index.html'
    context_object_name = 'trash_list'

    def get_queryset(self):
        """Return the trashes."""
        return TrashSetting.objects.order_by('-path_to_trash')


class DeleteView(generic.DetailView):
    model = TrashSetting
    template_name = 'trash/test.html'
