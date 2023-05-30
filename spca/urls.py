"""spca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from spca import views
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.spcahome,name='homepage'),
    path('aboutus/',views.aboutuz,name='aboutus'),
    path('contactus/',views.contactview,name='contactus'),
    path('commems/',include('spcacont.urls')),
    path('spcamems',include('spcacont.urls')),
    path('spcaevents/',include('spcacontents.urls'),name='spcaevents'),
     path('eventsgallery/',include('spcacontents.urls'),name='eventsgallery'),
     path('rescuegallery/',include('spcacontents.urls'),name='rescuegallery'),
     path('animallaw/',include('spcacontents.urls'),name='animallaw'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header  =  "SPCA Admin Panel"  
admin.site.site_title  =  "SPCA Admin Site"
admin.site.index_title  =  "SPCA Admin"
