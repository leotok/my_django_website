from django.contrib import admin

from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ('id', 'titulo', 'autor','texto','data_criacao', 'ultima_modificacao')
	list_per_page = 10
	search_fields = ['titulo', 'data_criacao']
	actions = None
