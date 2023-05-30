from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from spcanoti.models import Notifications
from spcacontents.models import HomeCover
from spca.forms import ContactForm
from spca.models import ContactData

def spcahome(request) :
	get_noti = Notifications.objects.all()
	get_crousel = HomeCover.objects.all()
	return render(request,'spcahomepage.html',{'noti':get_noti,'homecrousel':get_crousel})

def aboutuz(request):
	return render(request,'spcaabout.html')

def contactview(request):
	
	if request.method=='POST':
		formz = ContactForm(request.POST)
		
		if formz.is_valid():
			nm = formz.cleaned_data.get('fullname')
			em = formz.cleaned_data.get('email')
			ms = formz.cleaned_data.get('message')
			
			reg=ContactData(fullname=nm,email=em,message=ms)
			reg.save()

			formz=ContactForm()
			HttpResponseRedirect('/contactus/')
	else:
		formz=ContactForm()
	return render(request,'spcacontact.html',{'frm':formz})
