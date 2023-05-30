from django.urls import path
from spcacont import views
urlpatterns = [

	path('commems/',views.commemz,name='commems'),
	path('spcamems/',views.spcamemz,name='spcamems'),
]
