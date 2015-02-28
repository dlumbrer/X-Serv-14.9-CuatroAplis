#!/usr/bin/python


#!/usr/bin/python

class saludoApp:
	def parse(self, request, rest):
	    recurso = request.split()[1][1:]
	    #Recurso es o bien hola o bien adios
	    return recurso
		
	def process(self,parsedRequest):
	    if parsedRequest == "hola":
		return ("200 OK", "<html><body><h1>HOLA</h1></body></html>")
	    elif parsedRequest == "adios":
		return ("200 OK", "<html><body><h1>ADIOS</h1></body></html>")
