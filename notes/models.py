from django.db import models
from django.urls import reverse


# Create your models here.
class Notes(models.Model):
    note_type = models.CharField(max_length = 20)
    sub_category = models.CharField(max_length = 20)
    info_group = models.CharField(max_length = 50)
    info_title = models.CharField(max_length = 200)
    info_text = models.CharField(max_length = 100000)
    pic_file = models.FileField(blank=True,null=True)
    comment = models.CharField(max_length = 100000, blank = True, default = '')
    lang = models.CharField(max_length = 100, default = 'N')
    hhh = models.CharField(max_length = 4,default='1018')

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs = {'pk': self.pk})

    def __str__(self):
        return self.note_type



# Create your models here.
class Randomnotes(models.Model):
    info_text = models.CharField(max_length = 100000)
    pic_file = models.FileField(blank=True,null=True)
    hhh = models.CharField(max_length = 4,default='1018')

    def get_absolute_url(self):
        return reverse('notes:random_detail')