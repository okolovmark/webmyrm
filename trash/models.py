# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class TrashSetting(models.Model):
    path_to_log = models.CharField(default=".log_myrm_itislogfilemyrm_", max_length=200)
    path_to_trash = models.CharField(default=".mytrash", max_length=200)
    call_auto_cleaning_if_memory_error = models.BooleanField(default=False)
    dry = models.BooleanField(default=False)
    last_cleaning_date = models.DateTimeField(default=timezone.now())
    level_log = models.IntegerField(default=10)
    max_size_for_start_cleaning = models.IntegerField(default=2000000000)
    min_day_for_start_cleaning = models.IntegerField(default=14)
    policy = models.IntegerField(default=0)
    resolve_conflict = models.BooleanField(default=True)
    show_bar_status = models.BooleanField(default=False)
    silent = models.BooleanField(default=False)
    with_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return self.path_to_trash
