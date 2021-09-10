from django.views.generic.edit import UpdateView
from .models import Notes, Randomnotes
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect,HttpResponse
from .forms import NotesForm, RandomnotesForm
from django.http import Http404
import random
import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# get the current host url
from django.conf import settings
CUR_URL = getattr(settings, "CUR_URL", None)


def prism_helper(note_type):
    '''
    return the language and indicator for using prism.js
    '''

    if note_type == "Bash":
        my_lang = "bash"
    elif note_type == "Unix":
	    my_lang = "markup"
    elif note_type == "Pyspark":
        my_lang = "python"
    elif note_type == "Excel VBA":
        my_lang = "visual-basic"
    elif note_type == "Angular":
        my_lang = "html"
    elif note_type == "Web":
        my_lang = "html"
    elif note_type in ["Git", "Mongodb", "Others", "Shortcut", "Bloomberg"]:
        my_lang = "markup"
    else:
        my_lang = note_type.lower()

    return my_lang



def IndexView(request):
    # for http://.../notes/

    # get a list of note types
    l = list(Notes.objects.values_list('note_type').distinct())

    word_list = []
    size_l = [20,35,30,35]

    for e in l:
        word = e[0]
        if word in ["Python","Web"]:
            word_list.append({"key":word, "value":60*2, "href": word})
        else:
            word_list.append({"key":word, "value":size_l[random.randint(0,3)]*2, "href": word})

    context = {
        "word_list":word_list,
    }

    return render(request, 'notes/index.html', context)


def create_notes(request):
    # http://.../notes/add/

    form = NotesForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        if form["hhh"].value() == "1018":
            notes = form.save(commit=False)
            notes.save()
            return HttpResponseRedirect( CUR_URL + "notes/" + str(notes.pk))

    context = {
        "form": form,
    }

    return render(request, 'notes/view_notes_create.html', context)

def conitnue_notes(request, pk):
    # http://.../notes/{pk}/continue/

    form = NotesForm(request.POST or None, request.FILES or None)
    notes = Notes.objects.get(pk=pk)

    if form.is_valid():
        if form["hhh"].value() == "1018":
            notes = form.save(commit=False)
            notes.save()
            return HttpResponseRedirect( CUR_URL + "notes/" + str(notes.pk))

    context = {
        "form": form,
        "notes": notes,
    }

    return render(request, 'notes/view_notes_create.html', context)



class modify_notes(UpdateView):
    # http://.../notes/{pk}/modify_notes/

    model = Notes
    fields = ['note_type', 'sub_category', 'info_group','info_title', 'info_text', 'pic_file','comment','lang', 'hhh']

    def form_valid(self, form):
         if form["hhh"].value() != "1018":
             return self.render_to_response(self.get_context_data(form=form))
         else:
             return super(modify_notes, self).form_valid(form)

    # template_name_suffix = '_update'
    template_name ='notes/view_notes_update.html'


def DetailView(request, pk):
    # http://.../notes/{pk}/

    # get the note_type
    note = Notes.objects.filter(pk = pk)
    note_type = note.values_list('note_type').distinct()
    note_type = note_type[0][0]
    note_lang = note.values_list('lang').distinct()
    note_lang = note_lang[0][0]

    # get prism input
    if note_lang == "N":
        class_input = "language-" + prism_helper(note_type)
    else:
        class_input = "language-" + note_lang

    template= loader.get_template("notes/view_notes_detail.html")

    notes = Notes.objects.get(pk=pk)
    context = {
        'notes': notes,
        'pk': pk,
        'class_input': class_input
    }
    return HttpResponse(template.render(context, request))



def get_notes_data(all_data, all_group, num_group_per_page, page_num='1'):

    num_group = len(list(all_group))
    max_page = math.ceil(float(num_group)/num_group_per_page)
    all_page_nums = [ str(i) for i in range(1, max_page + 1)]

    if page_num not in all_page_nums:
        raise Http404

    all_group_from =(int(page_num) -1) * num_group_per_page
    all_group_to = min(num_group, (int(page_num) * num_group_per_page))
    all_group = all_group[all_group_from:all_group_to]
    all_data = [e for e in all_data if e.info_group in all_group]

    return all_data, all_group, str(int(page_num) + 1), page_num != all_page_nums[-1], max_page


def NotesView(request, note_type, page_num='1', sub_category = None, info_group = None):

    num_group_per_page = 5

    # note_type_new: cap inital letter
    note_type_new=note_type[0].upper()+note_type[1:]

    # ------------------------ for 3 different views of notes------------------------------
    # define:
    #        show_tc                    - show table of content link
    #        show_labels                - just a text label; make it look better
    #        all_data
    #        all_group
    # -------------------------------------------------------------------------------------

    if sub_category == None:
        # http://.../notes/{note_type}/

        show_tc = False
        show_labels = False

        # get all notes from this note type
        all_data = Notes.objects.filter(note_type = note_type_new)
        if len(all_data) == 0:
            raise Http404

        # get a list of group names based on note_type
        all_group_temp = list(Notes.objects.filter(note_type = note_type_new).values_list('info_group').distinct())
        all_group = [e[0] for e in all_group_temp]

    else:
        if info_group == None:

            # http://.../notes/{note_type}/{sub_category}

            show_tc = True
            show_labels = False

            all_data = Notes.objects.filter(note_type = note_type_new, sub_category = sub_category)
            if len(all_data) == 0:
                raise Http404

            all_group_temp = list(Notes.objects.filter(note_type = note_type_new, sub_category = sub_category).values_list('info_group').distinct())
            all_group = [e[0] for e in all_group_temp]
        else:
            # http://.../notes/{note_type}/{sub_category}/{info_group}

            show_tc = True
            show_labels = False

            all_data = Notes.objects.filter(note_type = note_type_new, sub_category = sub_category, info_group = info_group)
            if len(all_data) == 0:
                raise Http404

            all_group = [info_group]

    # get a list of sub cats based on note_type
    all_sub_cat_temp = list(Notes.objects.filter(note_type = note_type_new).values_list('sub_category').distinct())
    all_sub_cat = [e[0] for e in all_sub_cat_temp]

    # get prism input
    class_input = "language-" + prism_helper(note_type)

    all_data, all_group, next_page, has_next_page, max_page = get_notes_data(all_data, all_group, num_group_per_page, page_num)

    next_page_url = [e for e in request.path.split('/') if e]
    if next_page_url[-1].isdigit():
        next_page_url = next_page_url[:-1]
    next_page_url.append(next_page)
    next_page_url = '/'.join(next_page_url)

    template = loader.get_template('notes/view_notes.html')
    context = {
        'all_data': all_data,
        'all_sub_cat': all_sub_cat,
	    'note_type': note_type,
	    'sub_category': sub_category,
	    'info group': info_group,
	    'all_group': all_group,
		'note_type_new': note_type_new,
		'class_input': class_input,
		'show_tc': show_tc,
		'show_labels': show_labels,
        'next_page_url': next_page_url,
        'has_next_page': has_next_page,
        'next_page': next_page,
        'max_page': max_page,
        'page_num': page_num
    }

    return HttpResponse(template.render(context, request))



def NotesSubTC(request, note_type, sub_category):

	note_type_new=note_type[0].upper()+note_type[1:]

	all_data = Notes.objects.filter(note_type = note_type_new, sub_category = sub_category)

	all_group_temp = list(Notes.objects.filter(note_type = note_type_new, sub_category = sub_category).values_list('info_group').distinct())
	all_group = [e[0] for e in all_group_temp]

	template = loader.get_template('notes/view_notes_tc.html')
	context = {
        'all_data': all_data,
        'sub_category': sub_category,
		'all_group': all_group,
		'note_type': note_type,
		'note_type_new': note_type_new,
	}
	return HttpResponse(template.render(context, request))


























def create_random_notes(request):
    # http://.../notes/random_add/

    form = RandomnotesForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        if form["hhh"].value() == "1018":
            notes = form.save(commit=False)
            notes.save()
            return HttpResponseRedirect( CUR_URL + "notes/" + str(notes.pk))

    context = {
        "form": form,
    }

    return render(request, 'notes/create_random_notes.html', context)



class modify_random_notes(UpdateView):
    # http://.../notes/{pk}/random_modify/

    model = Randomnotes
    fields = ['info_text', 'pic_file','hhh']

    def form_valid(self, form):
         if form["hhh"].value() != "1018":
             return self.render_to_response(self.get_context_data(form=form))
         else:
             return super(modify_random_notes, self).form_valid(form)

    template_name_suffix = '_update_form'



def RandomView(request):

    all_data = Randomnotes.objects.all()

    template = loader.get_template('notes/notes_random_view.html')
    context = {
        'all_data': all_data,
    }
    return HttpResponse(template.render(context, request))
