from django import forms

class ContactForm(forms.Form):
	fullname=forms.CharField(widget=forms.TextInput(attrs={'name':'fullname','class':'form-control','placeholder':'Your Full Name....'}))
	email=forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email Address....'}))
	message=forms.CharField(widget=forms.Textarea(attrs={'name':'message','class':'form-control','placeholder':'Your Message Here....'}))
	
