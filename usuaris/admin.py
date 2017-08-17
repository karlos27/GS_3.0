from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import perfil, arxius

# Register your models here.

class perfilInline(admin.StackedInline):
	model = perfil
	can_delete = False

class arxiusInline(admin.StackedInline):
	model = arxius
	extra = 1
	
class UserAdmin(BaseUserAdmin):
	inlines = (perfilInline, arxiusInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)