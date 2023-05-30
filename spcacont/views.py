from django.shortcuts import render,HttpResponseRedirect
from .models import CommitteeMems,SpcaMembers
# Create your views here.

def commemz(request) :
	get_commems=CommitteeMems.objects.all()
	print(get_commems)
	return render(request,'commems.html',{'commems':get_commems})

def spcamemz(request):
	get_mems=SpcaMembers.objects.all()
	return render(request,'spcamems.html',{'spcamems':get_mems})
