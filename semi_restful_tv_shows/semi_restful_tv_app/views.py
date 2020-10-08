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
    pass
def createShow(request):
    pass

def readShow(request):
    pass


def editShow(request):
    pass
def updateShow(request):
    pass


def deleteShow(request):
    pass