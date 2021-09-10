from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.template import Context, loader
from django.http import HttpResponseRedirect,HttpResponse


import sys
sys.path.append('..')
from notes.models import Randomnotes
from random import randint

def IndexView(request):
    return render(request, 'notes_system/index.html')

def AboutView(request):
    return render(request, 'notes_system/about.html')

def view404(request, *args, **argv):
    all_data = Randomnotes.objects.all()
    notes = all_data[randint(0, len(all_data)-1)]

    context = {
        'notes': notes,
    }

    template = loader.get_template('notes_system/404.html')
    return HttpResponse(template.render(context, request))
