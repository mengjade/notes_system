from django import forms
from .models import Food
from .models import Excel

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['cook_name', 'cook_cat', 'tag' ,'cook_ing', 'info_text', 'comment', 'pic_file', 'hhh' ]


class ExcelForm(forms.ModelForm):
    class Meta:
        model = Excel
        fields = ['excel', 'hhh' ]
