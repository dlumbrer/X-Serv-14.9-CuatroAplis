#!/usr/bin/python


import random
import webapp

class aleatApp(webapp.app):
		
	def process(self, parsedRequest):
		return ("200 OK", "<html><body><h1>ALEATORIO</h1><p><a href='/aleat/"+
				str(random.randrange(10000000000000)) +
				"'>Dame Otra!!</a></p></body></html>")
