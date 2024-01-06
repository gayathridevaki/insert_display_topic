from django.shortcuts import render
from app.models import *

# Create your views here.
def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(Topic_Name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(Topic_Name=tn)
        WO=Webpage.objects.get_or_create(Topic_Name=TO,Name=na,Url=ur,Email=em)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'webpage':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    if request.method=='POST':
        pk=request.POST['pk']
        dt=request.POST['dt']
        at=request.POST['at']  
        WO=Webpage.objects.get(pk=pk)
        AO=AccessRecord.objects.get_or_create(Name=WO,Date=dt,Author=at)[0] 
        AO.save()
        QLAO=AccessRecord.objects.all()
        d1={'accessrecord':QLAO}
        return render(request,'display_accessrecord.html',d1)

    return render(request,'insert_accessrecord.html',d)


def select_multiple_topics(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(Topic_Name=i)
            d1={'webpage':QLWO}
            return render(request,'display_webpage.html',d1)
    return render(request,'select_multiple_topics.html',d)

def select_multiple_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    if request.method=='POST':
        name=request.POST.getlist('n')
        QLAO=AccessRecord.objects.none()
        for j in name:
            QLAO=QLAO|AccessRecord.objects.filter(name=j)
        d1={'accessrecord':QLAO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'select_multiple_webpage.html',d)





def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkbox.html',d)

