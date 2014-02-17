from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question
    def was_published_yesterday(self):
    	now = timezone.now()
        return  now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1) 
    was_published_yesterday.admin_order_field = 'pub_date'
    was_published_yesterday.boolean = True
    was_published_yesterday.short_description = 'Published 1 day ago?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text
