from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

toggle =0



class Snippet(models.Model):
    created = models.DateTimeField( default=timezone.now)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    on_hold = models.BooleanField(default=False)
    not_started = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    progress = models.IntegerField(default=toggle)
    start = models.DateField( default=timezone.now)
    end = models.DateField( default=timezone.now)
 


   

    def __str__(self):
        return self.title

class Tags(models.Model):
    tag = models.ForeignKey(Snippet, on_delete=models.CASCADE,related_name='tag')
    tag_text = models.CharField(max_length=200)
 

    def __str__(self):
        return self.tag_text
    
class Subgoals(models.Model):
    subgoals = models.ForeignKey(Snippet, on_delete=models.CASCADE,related_name='subgoals')
    subgoals_text = models.CharField(max_length=200)
  
    isCompleted = models.BooleanField(default=False)
 

    def __str__(self):
        return self.subgoals_text
    
        
