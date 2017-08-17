from __future__ import unicode_literals

import datetime
from django.utils import timezone

from django.db.models.signals import post_delete, post_save 
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class perfil(models.Model):
	nom_usuari = models.OneToOneField(User, on_delete=models.CASCADE)
	correu = models.EmailField('@')
	nif = models.CharField('NiF', max_length=9, blank= True, null=True)
	direcc = models.CharField('Adreça', max_length=100)
	pobl = models.CharField('Ciutat', max_length=9, blank= True, null=True)
	telf_1 = models.CharField('Telf.', max_length=9, blank= True, null=True)
	fax = models.CharField('Fax', max_length=9, blank= True, null=True)
	
	def __unicode__(self):
		return self.correu

	class Meta:
		ordering=['correu']
		verbose_name_plural= 'Dades addicionals'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        perfil.objects.create(nom_usuari=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()

class arxius(models.Model):
	usuari = models.ForeignKey('auth.User')
	nom_1=models.CharField('Nom arxiu', max_length=50, blank=True, null=True)
	arx_1 = models.FileField('PdF', upload_to='nomines', blank=True, null=True)
	data_pub = models.DateTimeField(default=timezone.now)
	
	def __unicode__(self):
		return self.nom_1

	def __str__(self):
		return self.nom_1

	class Meta:
		ordering=['-data_pub']
		verbose_name_plural= 'Descàrregues'

@receiver (post_delete, sender=arxius)
def arx_1_suprimit(sender, instance, **kwargs):
	instance.arx_1.delete(False)


