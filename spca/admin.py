from django.contrib import admin
from spca.models import ContactData
class ContactAdmin(admin.ModelAdmin):
	class Meta:
		model = ContactData

admin.site.register(ContactData,ContactAdmin)
