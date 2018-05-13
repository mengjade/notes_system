from django.shortcuts import render
from .forms import FoodForm
from django.views.generic.edit import UpdateView
from django.template import loader
from .models import Food, Storage, Planner
from django.http import HttpResponse
import urllib
import numpy as np



# Create your views here.

def IndexView(request):
    return render(request, 'food/index.html')


def create_notes(request):
    form = FoodForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        food = form.save(commit=False)
        food.save()
        return render(request, 'food/detail.html', {'food': food})
    context = {
        "form": form,
    }
    return render(request, 'food/create_notes.html', context)

class modify_notes(UpdateView):
    model = Food
    fields = ['cook_name', 'cook_cat', 'tag' ,'cook_ing', 'info_text',  'pic_file', 'comment' ]
    template_name_suffix = '_update_form'

def delete_notes(request, food_id):
    n = Food.objects.get(pk=food_id)
    n.delete()
    return render(request, 'food/index.html')

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
        if (e, urllib.parse.quote(e), c) not in all_cook_ing:
            all_cook_ing.append((e, urllib.parse.quote(e), c) )

    for e in all_cook_ing_meat_temp:
        c = all_cook_ing_meat_temp.count(e)
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
        c = all_tag_temp_temp.count(e)
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

    all_storage_data = Storage.objects.all()

    all_storage_type = list(Storage.objects.all().values_list('food_type').distinct())
    all_storage_type = [ e[0] for e in all_storage_type]
    all_p = list(Planner.objects.all())
    all_planner = []
    for e in all_p:
        l = []
        if e.ing is not None:
            a = (e.ing).split("，")
            for food_type in a:
                if food_type in all_storage_type:
                    l.append((food_type, "Y"))
                else:
                    l.append((food_type, "N"))
            all_planner.append([e.name,e.source,l])
	
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
        'all_storage_data': all_storage_data,
		'all_planner': all_planner,
        'complete': complete,
        'oneless': oneless,
    }
    return HttpResponse(template.render(context, request))
