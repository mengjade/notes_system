from django.db import models
from django.urls import reverse

# Create your models here.
class Food(models.Model):
    cook_ing = models.CharField(max_length = 50)
    cook_name = models.CharField(max_length = 20)
    cook_cat = models.CharField(max_length = 50)
    tag = models.CharField(max_length = 50, blank = True, null=True)
    info_text = models.CharField(max_length = 100000)
    pic_file = models.FileField(blank=True,null=True)
    comment = models.CharField(max_length = 100000,blank=True,null=True)
    hhh = models.CharField(max_length = 4,default='1018')

    def get_absolute_url(self):
        return reverse('food:detail', kwargs = {'pk': self.pk})

    def __str__(self):
        return (self.cook_name) + str(self.pk)


class Storage(models.Model):
    cat = models.CharField(max_length = 10)
    food_type = models.CharField(max_length = 10)
    quant = models.CharField(max_length = 10, blank = True, null=True)
    unit = models.CharField(max_length = 10, blank = True, null=True)
    expire_flag = models.CharField(max_length = 1, blank = True, null=True)

    def __str__(self):
        return (self.food_type) + str(self.quant)


class Planner(models.Model):
    name = models.CharField(max_length = 10)
    source = models.CharField(max_length = 10)
    ing = models.CharField(max_length = 50, blank = True, null=True)

    def __str__(self):
        return (self.name) + str(self.quant)

class Excel(models.Model):
    excel = models.FileField()
    hhh = models.CharField(max_length = 4,default='1018')

    def __str__(self):
        return (self.name) + str(self.quant)



