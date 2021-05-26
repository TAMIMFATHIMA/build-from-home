from django.shortcuts import render
from django.http import HttpResponse
from . models import audio

# Create your views here.
def index(request):
    Audios = audio.objects.all()
    return render(request,'index.html',{'Audios':Audios})
    #return HttpResponse("<h1>WELCOME TO TONAL</h1>")

def about(request):
    return HttpResponse("<h1>audio visualizer</h1>")

def Audio_store(request):
    if request.method == 'POST': 
        form = AudioForm(request.POST,request.FILES or None) 
        if form.is_valid(): 
            form.save() 
            return HttpResponse('successfully uploaded')
    else: 
        form = AudioForm() 
    return render(request, 'aud.htm', {'form' : form}) 