from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
from app.models import *

def display_form(request):
    if request.method=='POST':
        topic=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('data inserted')

    return render(request,'display_form.html')


def display_webpages(request):
    lot=Topic.objects.all()
    d={'tob':lot}

    if request.method=='POST':
        
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        TO=Topic.objects.get(topic_name=tn)
        
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('data submited')
    
    return render(request,'display_webpages.html',d)

def display_accessrecord(request):
    AO=Webpage.objects.all()
    d={'access':AO}
    if request.method=='POST':
        name=request.POST['topic']
        author=request.POST.get('author')
        date=request.POST.get('date')
        return HttpResponse('DAT SUBMITE SUCCESSFUlly')
    return render(request,'display_accessrecord.html',d)