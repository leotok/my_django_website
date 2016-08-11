from __future__ import unicode_literals

from django.db import models

class Post(models.Model):

	data_criacao		= models.DateTimeField(auto_now_add=True)
	ultima_modificacao 	= models.DateTimeField(auto_now=True)
	autor 				= models.CharField(max_length=64, null=True, blank=True)
	texto 				= models.TextField(null=True, blank=True)
	titulo				= models.TextField(unique=True)

