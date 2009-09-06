from django.db import models

import datetime, re
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from markdown import markdown
from tagging.fields import TagField

from django.contrib.auth.models import User

GAS_CHOICES = (
    ('Air', 21),
    ('EANx32', 32),
    ('EANx36', 36)
)

class Dive(models.Model):
    """docstring for Dive"""
    dive_number = models.IntegerField(max_length=4)
    dive_date = models.DateField()
    create_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    maxdepth = models.DecimalField('Maximum Depth', help_text='Feet or Meters', max_digits=4, decimal_places=1)
    time = models.IntegerField('Dive Time', max_length=3, help_text='Please enter time in minutes. Example: 54')
    gas = models.IntegerField(choices=GAS_CHOICES, default='Oxygen')
    avgdepth = models.DecimalField('Average Depth', help_text='Feet or Meters', max_digits=4, decimal_places=1, null=True, blank=True)
    water_temp = models.IntegerField('Water Temperature', max_length=2, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    comment_html = models.TextField(editable=False)
    tags = TagField()
    owner = models.ForeignKey(User, editable=False)

    def __unicode__(self):
        return self.comments