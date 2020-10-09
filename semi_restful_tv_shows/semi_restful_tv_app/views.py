from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    return redirect('/shows')


def home(request):
    context = {
        'allShows': Show.objects.all()
    }
    return render(request,'index.html', context)

def newShow(request):
    return render(request,'new_show.html')

def createShow(request):
    newShow = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc']
    )
    return redirect('/shows/'+str(newShow.id))

def readShow(request):
    pass


def editShow(request):
    pass
def updateShow(request):
    pass


def deleteShow(request):
    pass