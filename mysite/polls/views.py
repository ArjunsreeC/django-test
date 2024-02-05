from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.sessions.backends.db import SessionStore



def index(request):

	# s = SessionStore()
	# s['last_login'] = 1376587691
	# s.create()
	# s = SessionStore(session_key='2b1189a188b44ad18c35e113ac6ceead')
	request.session['lan'] = 'en'
	return HttpResponse("Session")