# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import *
from django.template.defaulttags import register

import requests
import json

def projects(request):

	projects = requests.get('https://api.github.com/users/leotok/repos')
	context = { 'projects': projects.json }

	return render(request, "projects.html", context)
