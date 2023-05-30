from django.contrib import admin
from .models import SpcaEvents,HomeCover,Rescues,RescuePhotos

class MyModelAdmin(admin.ModelAdmin):
	
	class Meta:
		model =SpcaEvents
		list_display = ('title', 'description')

class MyModelAdmin2(admin.ModelAdmin):
	class Meta:
		model = HomeCover
		list_display = ('hometitle0',)

class PhotoImageAdmin(admin.StackedInline):
	model = RescuePhotos

@admin.register(Rescues)
class PhotoAdmin(admin.ModelAdmin):
	inlines=[PhotoImageAdmin]
	class meta:
		Rescues

@admin.register(RescuePhotos)
class PhotoImageAdmin(admin.ModelAdmin):
	pass

admin.site.register(SpcaEvents, MyModelAdmin)
admin.site.register(HomeCover, MyModelAdmin)
