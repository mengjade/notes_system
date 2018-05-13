from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['cook_name', 'cook_cat', 'tag' ,'cook_ing', 'info_text', 'comment', 'pic_file' ]
