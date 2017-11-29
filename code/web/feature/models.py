# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class phash_feature(models.Model):
    _pic_url = models.CharField(max_length = 2048)
    _pic_wid = models.IntegerField()
    _pic_high = models.IntegerField()
    _pic_ratio = models.FloatField()
    _feat_x = models.IntegerField()
    _feat_y = models.IntegerField()
    _feat_x_range = models.IntegerField()
    _feat_y_range = models.IntegerField()
    _metadata = models.CharField(max_length = 255, default="")