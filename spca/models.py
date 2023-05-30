from django.db import models

class ContactData(models.Model):
	fullname=models.CharField(max_length=100)
	email=models.EmailField(max_length=50)
	message=models.TextField(max_length=500)
	
	def __str__(self):
		if self.fullname == None:
			return 'error'
		return self.fullname
