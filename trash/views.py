# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import TrashSetting
from django.shortcuts import render
import os
from myrm.main_logic import deleting_files


class IndexView(generic.ListView):
    template_name = 'trash/index.html'
    context_object_name = 'trash_list'

    def get_queryset(self):
        """Return the trashes."""
        return TrashSetting.objects.order_by('-path_to_trash')


class DetailTrashView(generic.DetailView):
    model = TrashSetting
    context_object_name = 'trash'
    template_name = 'trash/detail_trash.html'


def file_list(request, trashsetting_id):
    dir_list = []
    file_list = []
    folder = os.getcwd()

    for dirpath, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(dirpath, file)
            file_list.append(path)

        for dir in dirs:
            path = os.path.join(dirpath, dir)
            dir_list.append(path)
        break

    return render(request, 'trash/file_list.html', {
        'file_list': file_list,
        'dir_list': dir_list,
        'folder': folder,
    })

def delete_files(request, trashsetting_id):
