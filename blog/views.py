# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import *
from django.template.defaulttags import register
from .models import *

def blog(request):

	posts = Post.objects.all().order_by("-data_criacao")

	context = { 'posts':posts }

	return render(request, "blog.html", context)
