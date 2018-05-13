from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.template import Context, loader
from django.http import HttpResponseRedirect,HttpResponse

def IndexView(request):
    return render(request, 'notes_system/index.html')
