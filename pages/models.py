from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
    head = models.CharField(max_length=50, default='SOME ')
    date = models.DateField(blank=True, null=True,default=datetime.date.today)
    text = models.TextField(max_length=1000)
    classes = models.BooleanField(default = False)
    fm   = models.BooleanField(default= False)

    def __str__(self):
        return self.head[:20]