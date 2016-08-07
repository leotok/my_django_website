# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import *
from django.template.defaulttags import register
from .models import *

# Create your views here.

def home(request):

	return render(request, "home.html")
