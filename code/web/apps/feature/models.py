# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class phash_feature(models.Model):
    _category = models.CharField(max_length = 512)
    _tags = models.CharField(max_length = 1024)
    _pic_url = models.CharField(max_length = 2048)
    _pic_wid = models.IntegerField()
    _pic_high = models.IntegerField()
    _pic_ratio = models.FloatField()
    _feat_x = models.IntegerField()
    _feat_y = models.IntegerField()
    _feat_w = models.IntegerField()
    _feat_h = models.IntegerField()
    _feat_x_range = models.IntegerField()
    _feat_y_range = models.IntegerField()
    _dist = models.FloatField()
    _metadata = models.CharField(max_length = 1024, default="")
    class Meta:
        db_table = 'phash_feature'

class template_feature(models.Model):
    _category = models.CharField(max_length=512)
    _tags = models.CharField(max_length = 1024)
    _pic_url = models.CharField(max_length=2048)
    _pic_wid = models.IntegerField()
    _pic_high = models.IntegerField()
    _pic_ratio = models.FloatField()
    _feat_x = models.IntegerField()
    _feat_y = models.IntegerField()
    _feat_w = models.IntegerField()
    _feat_h = models.IntegerField()
    _deva = models.IntegerField()
    _mcnt = models.IntegerField()
    _metadata = models.CharField(max_length = 1024, default="")
    class Meta:
        db_table = 'template_feature'