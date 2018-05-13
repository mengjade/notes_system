from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Notes(models.Model):
    note_type = models.CharField(max_length = 20)
    sub_category = models.CharField(max_length = 20)
    info_group = models.CharField(max_length = 50)
    info_title = models.CharField(max_length = 200)
    info_text = models.CharField(max_length = 100000)
    pic_file = models.FileField(blank=True,null=True)
    comment = models.CharField(max_length = 100000,blank=True,null=True)
 
    def get_absolute_url(self):
        return reverse('notes:detail', kwargs = {'pk': self.pk})    
   
    def __str__(self):
        return self.note_type
