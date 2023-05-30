from django.db import models

# Create your models here.
class CommitteeMems(models.Model):
	sl_id=models.AutoField(primary_key=True)
	commem = models.CharField(max_length=100)
	comprof=models.CharField(max_length=150)
	
	def __str__(self):
		if self.commem==None:
			return "ERROR-CUSTOMER NAME IS NULL"
		return self.commem

class SpcaMembers(models.Model):
	sl_idz = models.AutoField(primary_key=True)
	spcamems=models.CharField(max_length=100,default='null')
	memsloca=models.CharField(max_length=100)
	
	def __str__(self):
		if self.spcamems==None:
			return "ERROR-CUSTOMER NAME IS NULL"
		return self.spcamems
	

	
