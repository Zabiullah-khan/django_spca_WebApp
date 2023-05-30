from django.shortcuts import render,get_object_or_404
from .models import SpcaEvents,RescuePhotos
# Create your views here.

def spcaevent(request):
	get_events = SpcaEvents.objects.all()
	return render(request,'spcaevents.html',{'events':get_events})

def eventsgal(request,id):
	get_event_jpg = get_object_or_404(SpcaEvents,pk=id)
	return render(request,'eventsgallery.html',{'eventjpg':get_event_jpg})

def rescuegal(request):
	get_rescue_gal=RescuePhotos.objects.all()
	return render(request,'rescuegallery.html',{'rescuegal':get_rescue_gal})

def animalrights(request):
	return render(request,'animalrights.html')
