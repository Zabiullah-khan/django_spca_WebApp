from django.db import models
# Create your models here.		


class HomeCover(models.Model):
	homecovers='Home-Covers'
	hometitle0=models.CharField(max_length=100)
	homecover0=models.ImageField(blank=True,upload_to='homecovers/')
	
	hometitle1=models.CharField(max_length=100)
	homecover1=models.ImageField(blank=True,upload_to='homecovers/')
	
	hometitle2=models.CharField(max_length=100)
	homecover2=models.ImageField(blank=True,upload_to='homecovers/')
	
	def __str__(self):
		
		return self.homecovers
	
		
	
class SpcaEvents(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	coverphoto = models.ImageField(blank=True,upload_to='covers/')
	image1 = models.ImageField(blank=True,upload_to='images/')
	image2 = models.ImageField(blank=True,upload_to='images/')
	image3 = models.ImageField(blank=True,upload_to='images/')
	image4 = models.ImageField(blank=True,upload_to='images/')
	image5 = models.ImageField(blank=True,upload_to='images/')
	image6 = models.ImageField(blank=True,upload_to='images/')
	image7 = models.ImageField(blank=True,upload_to='images/')
	image8 = models.ImageField(blank=True,upload_to='images/')
	image9 = models.ImageField(blank=True,upload_to='images/')
	image10 = models.ImageField(blank=True,upload_to='images/')
	
	def __str__(self):
		if self.title==None:
			return 'error'
		return self.title

class Rescues(models.Model):
	image=models.ImageField(blank=True,upload_to='rescues')

class RescuePhotos(models.Model):
	posts=models.ForeignKey(Rescues,default=None,on_delete=models.CASCADE)
	image=models.ImageField(blank=True,upload_to='rescues/')

	
