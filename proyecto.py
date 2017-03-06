# -*- coding: utf-8 -*-
import os.path as path

class objeto():
    def menu(self):
        print "\n \n"
        print "BIENVENIDO \n"
        print "1. Agregar \n"
        print "2. Mostrar \n"
        print "3. Editar \n"
        print "4. Salir \n"
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
        for i in range(cantidad):
            archivo.seek(finalArchivo)
            nombre = str(raw_input("Nombre:")) 
            apellido = str(raw_input("Apellido:"))
            cedula = str(raw_input("Cedula:")) 
            edad = str(raw_input("Edad:")) 
            codigo = str(raw_input("Codigo del empleado:"))
            estado = int(raw_input("si esta activo marque 1 si no masrque 0:"))
            while estado > 1:
                estado = int(raw_input("por favor marque como se le indico arriba necio:"))
            estado = str(estado)
            datos = [cedula, " , ", nombre," , ",apellido," , ", edad," , ", codigo," , ", estado , "\n"]
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
            masEmpleados = []
            for line in archivo.readlines():
                array = line.split(',')
                # print array

                if array != "['\n']":
                    arrayCedula = array[0]
                    # print arrayCedula
                    #Esta es la cedula del array
                    arrayCedula = int(arrayCedula)
                    # print type(arrayCedula)

                    if cedula == arrayCedula:
                        print "\n"
                        print "Que quiere modificar:"
                        print "Nombre = 1."
                        print "Apellido = 2."
                        print "Edad = 3."
                        print "Codigo = 4."
                        print "\n"
                        mini = int(raw_input("Que quieres modificar:"))
                        while mini == 0 or mini > 5:
                            mini = int(raw_input("Por favor marque como se le indica arriba:"))
                        
                        if mini == 1:
                            nombre = str(raw_input("Nombre:"))
                            newCedula = str(array[0])
                            datos = [newCedula, " , ", nombre," , ",array[2]," , ", array[3]," , ", array[4]," , ", array[5]]
                            masEmpleados.append(datos)
                            print "\n"
                            print "Se modifico el nombre de la persona."
                            print "\n"
                        
                        if mini == 2:
                            apellido = str(raw_input("Apellido:"))
                            newCedula = str(array[0])
                            datos = [newCedula, " , ", array[1]," , ",apellido," , ", array[3]," , ", array[4]," , ", array[5]]
                            masEmpleados.append(datos)
                            print "\n"
                            print "Se modifico el apellido de la persona."
                            print "\n"

                        if mini == 3:
                            Edad= str(raw_input("Edad:"))
                            newCedula = str(array[0])
                            datos = [newCedula, " , ", array[1]," , ",array[2]," , ", edad," , ", array[4]," , ", array[5]]
                            masEmpleados.append(datos)
                            print "\n"
                            print "Se modifico la edad de la persona."
                            print "\n"

                        if mini == 4:
                            codigo = str(raw_input("Codigo:"))
                            newCedula = str(array[0])
                            datos = [newCedula, " , ", array[1]," , ",array[2]," , ", array[3]," , ", codigo," , ", array[5]]
                            masEmpleados.append(datos)
                            print "\n"
                            print "Se modifico el codigo de la persona."
                            print "\n"
                            
                    else:
                        # masEmpleados.append(array)
                        datos = [array[0], " , ", array[1]," , ",array[2]," , ", array[3]," , ", array[4]," , ", array[5], "\n"]
                        masEmpleados.append(datos)
        else:
            print "No exixte ese numero de cedula."
            print "\n"
        print masEmpleados
        file = open("texto2.txt", "w+")
        for datos in masEmpleados:
            finalArchivo = file.tell()
            file.seek(finalArchivo)
            file.writelines(datos)
            file.seek(finalArchivo)

        menu = data.menu()
        data.opcciones(menu)



    def opcciones(self, menu):
        if menu == 1:
            data1 = data.entra(menu)
            procesa1 = data.procesa(data1)
        if menu == 2:
            data.mostrar()

        if menu == 4:
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
    
        if menu == 3:
            data.editar()


data = objeto()
#menu = data.menu()




def mein():
    menu = data.menu()
    data.opcciones(menu)



            

