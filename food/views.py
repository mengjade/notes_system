from django.shortcuts import render
from .forms import FoodForm, ExcelForm
from django.views.generic.edit import UpdateView
from django.template import loader
from .models import Food, Storage, Planner
from django.http import HttpResponse
import urllib

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

import os
from subprocess import call
import pandas as pd


# get the current host url
from django.conf import settings
CUR_PATH = getattr(settings, "CUR_PATH", None)


# Create your views here.

def IndexView(request):
    return render(request, 'food/index.html')

def create_notes(request):
    form = FoodForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        if form["hhh"].value() == "1018":
            food = form.save(commit=False)
            food.save()
            return render(request, 'food/detail.html', {'food': food})
    context = {
        "form": form,
    }
    return render(request, 'food/create_notes.html', context)

class modify_notes(UpdateView):
    model = Food
    fields = ['cook_name', 'cook_cat', 'tag' ,'cook_ing', 'info_text',  'pic_file', 'comment', 'hhh']

    def form_valid(self, form):
     if form["hhh"].value() != "1018":
         return self.render_to_response(self.get_context_data(form=form))
     else:
         return super(modify_notes, self).form_valid(form)

    template_name_suffix = '_update_form'

def DetailView(request, pk):
    template= loader.get_template("food/detail.html")
    food = Food.objects.get(pk=pk)
    context = {
        'food': food,
        'pk': pk,
    }
    return HttpResponse(template.render(context, request))


def RecipeView(request):

    all_data = Food.objects.all()

    all_cook_cat_temp = list(Food.objects.all().values_list('cook_cat').distinct())
    all_cook_cat = [(e[0], urllib.parse.quote(e[0])) for e in all_cook_cat_temp]

    template = loader.get_template('food/recipe_view.html')
    context = {
        'all_data': all_data,
        'all_cook_cat': all_cook_cat,
    }
    return HttpResponse(template.render(context, request))

def RecipeIngView(request):

    meat_l = ['牛肉卷' ,'猪肉末', '五花肉', '鸡翅' ,'花蛤', '鸡肉','虾','培根', '三文鱼',
              '扇贝', '里脊','牛腩', '腊肉', '火腿','咸肉', '牛肉', '排骨', '鱿鱼', '肉丸',
              '午餐肉' '牛腱','鱼条', '牛尾' '鳗鱼', '猪颈肉','猪肉',"虾米"]

    all_data = Food.objects.all()

    all_cook_ing_temp = list(Food.objects.all().values_list('cook_ing'))



    # translate into list
    all_cook_ing_other_temp = []
    all_cook_ing_meat_temp = []

    for e in all_cook_ing_temp:
        a = e[0].split("，")
        for e1 in a:
            if e1 != "" and e1 not in ["葱","姜","蒜","无","洋葱","尖椒","红椒","青椒","甜品"]:
                if e1 in meat_l:
                    all_cook_ing_meat_temp.append(e1)
                else:
                    all_cook_ing_other_temp.append(e1)

    all_cook_ing_meat_temp.sort()
    all_cook_ing_other_temp.sort()

    # count and add in tuples
    all_cook_ing = []
    all_cook_ing_meat= []

    for e in all_cook_ing_other_temp:
        c = all_cook_ing_other_temp.count(e)
        c = str(c)
        if (e, urllib.parse.quote(e), c) not in all_cook_ing:
            all_cook_ing.append((e, urllib.parse.quote(e), c) )

    for e in all_cook_ing_meat_temp:
        c = all_cook_ing_meat_temp.count(e)
        c = str(c)
        if (e, urllib.parse.quote(e), c) not in all_cook_ing_meat:
            all_cook_ing_meat.append((e, urllib.parse.quote(e), c) )

    template = loader.get_template('food/by_ing_view.html')
    context = {
        'all_data': all_data,
        'all_cook_ing': all_cook_ing,
        'all_cook_ing_meat': all_cook_ing_meat,
    }
    return HttpResponse(template.render(context, request))

def RecipeTagView(request):

    all_data = Food.objects.all()

    all_tag_temp = list(Food.objects.all().values_list('tag'))

    all_tag_temp_temp = []

    for e in all_tag_temp:
        if e[0] is not None:
            a = e[0].split("，")
            for e1 in a:
                if e1 != "None" and e1 != "":
                    all_tag_temp_temp.append(e1)

    all_tag_temp_temp.sort()
    all_tag_temp_temp.sort(key=len)

    all_tag = []
    for e in all_tag_temp_temp:
        c = str(all_tag_temp_temp.count(e))
        if (e,urllib.parse.quote(e),c) not in all_tag:
            all_tag.append((e,urllib.parse.quote(e),c))

    template = loader.get_template('food/by_tag_view.html')
    context = {
        'all_data': all_data,
        'all_tag': all_tag,
    }
    return HttpResponse(template.render(context, request))

def RecipeSubView(request, search_type, search_value):

    search_value = urllib.parse.unquote(search_value)

    if search_type == "cook_cat":
        all_data = Food.objects.filter(cook_cat = search_value)

    if search_type == "cook_ing":
        all_data = Food.objects.filter(cook_ing__icontains = search_value)

    if search_type == "tag":
        all_data = Food.objects.filter(tag__icontains = search_value)

    template = loader.get_template('food/recipe_sub_view.html')
    context = {
        'all_data': all_data,
        'search_value': search_value
    }
    return HttpResponse(template.render(context, request))

def SweetView(request):

    all_data = Food.objects.filter(cook_cat = "甜品")

    template = loader.get_template('food/sweet_view.html')
    context = {
        'all_data': all_data,
    }
    return HttpResponse(template.render(context, request))

def WTCView(request):

    # get food_storage table
    df = pd.read_excel(open(CUR_PATH + "media/Tracker_v2.0.xlsx" ,'rb'), parse_cols = "A:E",
           sheetname='Food_Track',names=['cat','food_type','quant','unit','inputdate'],header=None)
    df = df[1:]
    df = df.dropna(how="all")

    df1 = pd.read_excel(open(CUR_PATH + "media/Tracker_v2.0.xlsx" ,'rb'), parse_cols = "G:H",
           sheetname='Food_Track',names=['cat','food_type'],header=None)
    df1 = df1[1:]
    df1 = df1.dropna()

    df = pd.concat([df,df1])
    df = df.fillna(" ")
    df = df[['cat','food_type','quant','unit']]
    all_storage_type = df.food_type.tolist()
    storagetable = df.to_html(index = False,header = False)

    # get planner table
    df2 = pd.read_excel(open(CUR_PATH + "media/Tracker_v2.0.xlsx" ,'rb'), parse_cols = "L:N",sheetname='Food_Track',names=['name','source','ing'],header=None)
    df2 = df2.dropna()
    df2 = df2.values.tolist()
    for i,r in enumerate(df2):
        ing_l = r[2].split(",")
        to_add = []
        for j,ing in enumerate(ing_l):
            if ing in all_storage_type:
                s = "Y"
            else:
                s = "N"
            to_add.append([ing, s])
        df2[i][2] = to_add.copy()

    # get to-get list
    df3 = pd.read_excel(open(CUR_PATH + "media/Tracker_v2.0.xlsx" ,'rb'), parse_cols = "J",sheetname='Food_Track')
    df3 = df3.togetfood.tolist()

	# recommendations
    all_reci = Food.objects.all().exclude(cook_cat="甜品")
    complete = []
    oneless = []
    for e in all_reci:
        l = []
        s = 0
        ing = (e.cook_ing).split("，")

        for a in ing:
            if a in all_storage_type:
                s = s + 1
                l.append((a, "Y"))
            else:
                l.append((a, "N"))

        if s == len(l):
            complete.append((e.cook_name, l,e.pk))
        if s == (len(l) - 1):
            oneless.append((e.cook_name, l,e.pk))


    template = loader.get_template('food/wtc_view.html')
    context = {
        'complete': complete,
        'oneless': oneless,
        'storagetable': "<table class='table'>"+ storagetable[36:],
        'df2':df2,
        'df3':df3
    }
    return HttpResponse(template.render(context, request))



def update_storage_view(request):

    form = ExcelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        if form["hhh"].value() == "1018":

            os.remove(CUR_PATH + "media/Tracker_v2.0.xlsx")

            excel = form.save(commit=False)
            excel.save()

            return HttpResponseRedirect("food/whattocook/")
            #return render(request, 'food/wtc_view.html')

    context = {"form": form,}
    return render(request, 'food/storage_update_form.html', context)





