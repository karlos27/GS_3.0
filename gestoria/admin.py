from django.contrib import admin

from .models import noticia

# Register your models here.

class nAdmin(admin.ModelAdmin):
	list_display = ['data_pub', 'titol', 'font']
	list_filter = ['data_pub']
	search_fields = ['titol', 'font']

admin.site.register(noticia, nAdmin)