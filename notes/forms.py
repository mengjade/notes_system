from django import forms
from .models import Notes, Randomnotes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note_type','sub_category','info_group','info_title','info_text','pic_file','comment','lang','hhh']

class RandomnotesForm(forms.ModelForm):
    class Meta:
        model = Randomnotes
        fields = ['info_text','pic_file','hhh']
