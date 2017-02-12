# -*- coding: utf-8 -*-
import os.path as path

class objeto():
	def menu(self):
		print "Bienvenido"
		ver = 0
		alistar = 1
		salir = 2
		print "1. Agregar \n"
		print "2. Mostrar \n"
		print "3. Salir"
		menu = int(raw_input("que opcion quieres:"))
		return menu
		
	def entra(self, menu):
		if path.exists("texto2.txt"):
			cantidad = int(raw_input("cantidad de empleados:"))
		else:
			open("texto2.txt", "a")
			cantidad = int(raw_input("cantidad de empleados:"))
		lista = [cantidad]
		return lista
		
	def procesa(self, lista):
		cantidad = lista[0]
		archivo = open("texto2.txt", "r+")
		finalArchivo = archivo.tell()
		# contenido = archivo.read()
		# print contenido
		archivo.seek(finalArchivo)
		for i in range(cantidad):
			nombre = str(raw_input("Nombre:")) 
			apellido = str(raw_input("Apellido:")) 
			edad = str(raw_input("Edad:")) 
			codigo = str(raw_input("Codigo del empleado:"))
			estado = int(raw_input("si esta activo marque 1 si no masrque 0:"))
			while estado > 1:
				estado = int(raw_input("por favor marque como se le indico arriba necio:"))
			estado = str(estado)
			datos = [nombre," , ",apellido," , ", edad," , ", codigo," , ", estado , '\n']

		archivo.writelines(datos)
		archivo.seek(finalArchivo)
		# newContent = archivo.read()
		# print newContent

	def mostrar(self):
		archivo = open("texto1.txt", "r+")
		contenido = archivo.read()
		print contenido

data = objeto()

menu = data.menu()

def mein():
	if menu == 1:
		data1 = data.entra(menu)
		procesa1 = data.procesa(data1)
	if menu == 2:
		data.mostrar()

			

