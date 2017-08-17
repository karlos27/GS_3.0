from __future__ import unicode_literals

import datetime

from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField

# Create your models here.

class noticia(models.Model):
	id_noticia = models.AutoField(primary_key=True)
	titol = models.CharField('Head', max_length=100)
	cos = RichTextField('Body')
	font = models.URLField('Source', blank=True, null=True)
	data_pub = models.DateTimeField('Publication Date', default=timezone.now)
	foto = models.ImageField(upload_to='fotografies', blank=True, null=True)

	def __unicode__(self):
		return u'%s' % (self.titol)

	def __str__(self):
		return u'%s' % (self.titol)

	class Meta:
		ordering = ['-data_pub']
		verbose_name_plural = 'News'

@receiver(post_delete, sender=noticia) 
def foto_suprimida(sender,instance,**kwargs):
	instance.foto.delete(False)