from django.urls import path
from spcacontents import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns= [
	
	path('spcaevents',views.spcaevent,name='spcaevents'),
	path('eventsgallery/<int:id>/',views.eventsgal,name='eventsgallery'),
	path('rescuegallery',views.rescuegal,name='rescuegallery'),
	path('animallaw',views.animalrights,name='animallaw')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
