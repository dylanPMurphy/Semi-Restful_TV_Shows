from django.shortcuts import render, redirect, HttpResponse
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
    if request.method == "POST":
        newShow = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            desc = request.POST['desc']
        )
    return redirect('/shows/'+str(newShow.id))

def readShow(request, show_id):

    context={
        'selected_show': Show.objects.get(id=show_id)
    }
    return render(request,'show_profile.html', context)


def editShow(request, show_id):
    context={
        'selected_show': Show.objects.get(id=show_id) 
    }
    return render(request, 'edit_show.html', context)

def updateShow(request, show_id):
    if request.method == "POST":
        selected_show = Show.objects.get(id=show_id)
        selected_show.title = request.POST['title']
        selected_show.network = request.POST['network']
        selected_show.release_date = request.POST['release_date']
        selected_show.desc = request.POST['desc']
        selected_show.save()
    return redirect('/shows/'+str(show_id))

def deleteShow(request, show_id):
    if request.method == "POST":
        selected_show = Show.objects.get(id=show_id)
        selected_show.delete()
    return redirect('/')