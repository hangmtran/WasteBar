from django.http import HttpResponse

# from django.template import loader
# from .models import Donators


# def index(request):
#     return HttpResponse("Hello")
#     latest_food_list = Donators.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('pickmywaste/index.html')
#     context = {
#         'latest_food_list': latest_food_list,
#     }
#     return HttpResponse(template.render(context, request))

from django.shortcuts import render, get_object_or_404

from .models import Food, Donators

from .forms import CreateNewListing


def index(request):
    ls = Food.objects.get(id=id)
    latest_food_dict = {}
    latest_food_list = Food.objects.order_by('-pub_date')[:5]
    context = {'latest_food_list': latest_food_list}
    return render(request, 'pickmywaste/index.html', context)



def detail(request, donator_id):
   
    donator = get_object_or_404(Donators, pk=donator_id)
    return render(request, 'pickmywaste/.html', {'donator': donator})

# def results(request, donator_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % donator_id)

# def take(request, donator_id):
#     return HttpResponse("You're taking %s." % donator_id)

def foodMap(response):
    return render(response,"pickmywaste/foodMap.html", {})

#function for form food listing
def create(response):
    #check to see if post or get request(default is always get)
    if response.method == "POST": 
        form = CreateNewListing(response.POST)
        if form.is_valid():
            n = form.cleaned_data["title"] #form takes post and takes data, and use 
            t = Food(name
    else:
        form = CreateNewListing()#create a blank form and pass to HTML
    return render(response,"pickmywaste/create.html",{"form":form})
