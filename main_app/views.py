from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .models import House, Feature
from .forms import HouseSpaceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


class HouseCreate(CreateView):
    model = House
    fields = '__all__' #double underscore
    success_url = '/houses/'

class HouseUpdate(UpdateView):
    model = House
    fields = ['price', 'special_note']

class HouseDelete(DeleteView):
    model = House
    success_url = '/houses/'

def home(request):
    return HttpResponse('<h1>Hello Lili </h1>')



def about(request):
    return render(request, 'about.html')

def houses_index(request):
    houses = House.objects.all()
    return render(request, 'houses/index.html', {'houses': houses})

def house_details(request, house_id): # refer to the id we define in our urls.py
    house = House.objects.get(id=house_id)
    housespace_form = HouseSpaceForm()
    return render(request, 'houses/detail.html', {
        'house': house, 'housespace_form': housespace_form 
        
        })


def add_housespace(request, house_id):
    #create a modelform instance usig the data in request.POSTT
    form = HouseSpaceForm(request.POST)
    #check if the form is valid
    if form.is_valid():
        new_space = form.save(commit=False)
        new_space.house_id = house_id
        new_space.save()
    return redirect('detail', house_id=house_id)




#Features CRUB Operations

class FeatureList(ListView):
    model = Feature


class FeatureDetail(DetailView):
    model = Feature


