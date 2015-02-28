#!/usr/bin/python

class sumaApp:
	def parse(self, request, rest):
		paquete = rest.split('/')[1:]
		# paquete es una lista con [num1, num2]
		return paquete
		
	def process(self,parsedRequest):
	    try:
		suma = int(parsedRequest[0]) + int(parsedRequest[1])
		return ("200 OK", "<html><body><h1>" +
                          "La suma es" +
                          "</h1><p>" + parsedRequest[0] + " + " + parsedRequest[1] + " = " + str(suma) + "</body></html>")
	    except ValueError:
		return ("200 OK", "<html><body><h1>Has metido mal los operandos</html></body></h1>")
	    except IndexError:
		return ("200 OK", "<html><body><h1>Mal uso, uso: /suma/op1/op2</html></body></h1>")
