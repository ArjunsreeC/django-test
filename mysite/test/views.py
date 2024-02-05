from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore



def index(request):

	# s = SessionStore()
	# s = Session.objects.get(pk='2b1189a188b44ad18c35e113ac6ceead')
	# x = str(s.session_data)
	lan = request.session['lan']
	return HttpResponse(lan)