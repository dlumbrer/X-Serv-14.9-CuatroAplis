#!/usr/bin/python


import suma
import hola
import aleat
import webapp

if __name__ == "__main__":
    saludo = hola.saludoApp()
    sumar = suma.sumaApp()
    aleatorio = aleat.aleatApp()
    testWebApp = webapp.webApp("localhost", 1234, {'/hola': saludo,
                                            '/adios': saludo,
                                            '/suma': sumar,
                                            '/aleat': aleatorio})
