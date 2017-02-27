# -*- coding: utf-8 -*-
import os.path as path

class objeto():
    def menu(self):
        print "BIENVENIDO \n"
        print "1. Agregar \n"
        print "2. Mostrar \n"
        print "3. salir \n"
        print "4. Editar \n"
        menu = int(raw_input("Que opcion quieres:"))
        print "\n"
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
        archivo = open("texto2.txt", "a")
        finalArchivo = archivo.tell()
        # contenido = archivo.read()
        # print contenido
        archivo.seek(finalArchivo)
        for i in range(cantidad):
            nombre = str(raw_input("Nombre:")) 
            apellido = str(raw_input("Apellido:"))
            cedula = str(raw_input("Cedula:")) 
            edad = str(raw_input("Edad:")) 
            codigo = str(raw_input("Codigo del empleado:"))
            estado = int(raw_input("si esta activo marque 1 si no masrque 0:"))
            while estado > 1:
                estado = int(raw_input("por favor marque como se le indico arriba necio:"))
            estado = str(estado)
            datos = [cedula, " , ", nombre," , ",apellido," , ", edad," , ", codigo," , ", estado , '\n']
            archivo.writelines(datos)
            archivo.seek(finalArchivo)
        menu = data.menu()
        data.opcciones(menu)
        # newContent = archivo.read()
        # print newContent

    def mostrar(self):
        archivo = open("texto2.txt", "r")
        contenido = archivo.read()
        print contenido
        menu = data.menu()
        data.opcciones(menu)

    def editar(self):
        cedula = int(raw_input("Numero De Cedula:"))

        if cedula > 1:
            archivo = open("texto2.txt", "r")
            i = 0;
            for line in archivo.readlines():
                array = line.split(',')
                # print array
                arrayCedula = array[0]
                arrayCedula = int(arrayCedula)
                # print type(arrayCedula)
                # print type(cedula)
                # print "Esta es la cedula ->", cedula
                if cedula == arrayCedula:
                    nombre = str(raw_input("Nombre:"))

                    datos = [cedula, " , ", nombre," , ",array[2]," , ", array[3]," , ", array[4]," , ", array[5] , '\n']
                    masEmpleados[i] = datos
                    i += 1
                else:
                    masEmpleados[i] = array
                    i += 1

            archivo = open("texto2.txt", "w+")
            finalArchivo = archivo.tell()
            # contenido = archivo.read()
            # print contenido
            archivo.seek(finalArchivo)
            for datos in masEmpleados:
                archivo.writelines(datos)
                archivo.seek(finalArchivo)



    def opcciones(self, menu):
        if menu == 1:
            data1 = data.entra(menu)
            procesa1 = data.procesa(data1)
        if menu == 2:
            data.mostrar()

        if menu == 3:
            repetir = 1
            while repetir != 0:
                print "Si en verdad deseas salir marque 0 si deseas volver a las opcciones marque 1:\n"
                repetir = int(raw_input("1 o 0:"))
                if repetir == 1:
                    data.menu()
                print "\n"
                while repetir > 1:
                    print "Por favor marque como se le indica arriba gracias.\n"
                    repetir = int(raw_input("1 o 0:\n"))
                    if repetir == 1:
                        data.menu()
    
        if menu == 4:
            data.editar()


data = objeto()
#menu = data.menu()




def mein():
    menu = data.menu()
    data.opcciones(menu)



            

