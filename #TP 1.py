#TP 1
import getpass
import os

admin = "a"
contraseña = "a"

cerrar = True
cont = 0
opcion = -1
menuAdmin = """
=========================
MENU DE ADMINISTRADOR
1. Gestionar Aerolineas
2. Aprobar/Denegar Promocion
3. Gestionar Novedades
4. Reportes
5. Salir
=========================
"""
gestionAerolinea ="""
=========================
Gestionar Aerolineas
a. Crear Aerolineas
b. Modificar Aerolineas
c. Eliminar Aerolineas
d. Volver")
=========================
"""

while cerrar == True :
    tu_usu = "a" #input("Ingrese Usuario: ")
    tu_cont = "a" #input("Ingrese contraseña:") #getpass.getpass("Ingrese contraseña")
    while (tu_usu != admin or tu_cont != contraseña) and cont < 2:
        print("Usuario y/o contraseña erroneo")
        cont +=1
        tu_usu = input("Ingrese Usuario: ")
        tu_cont = input("Ingrese contraseña:")
    if cont == 3:
        print("3 intentos fallidos. El programa se cerrara")
        opcion = input("Presione enter para salir")

    if tu_usu == admin and tu_cont == contraseña:
        os.system("cls")
        
        while opcion != "5":
            print(menuAdmin)
            opcion = input("Ingrese opcion: ")
            while opcion >= "1" or opcion <= "4":
                os.system("cls")
                if opcion == "1":
                    print(gestionAerolinea)
                    while opcion != "d":
                        opcion = input("Ingrese opcion: ")
                        os.system("cls")
                        if opcion == "a":
                            while opcion != "n":
                                #crea aerolina
                                crearAerolinea = input("Ingrese aerolina: ")
                                crearOtra = input("Desea crear otra aerolina? s/n: ")
                                if crearOtra == "s":
                                    os.system("cls")
                                    crearAerolinea = input("Ingrese aerolina: ")
                                else :
                                    os.system("cls")
                                    opcion = "n"
                                    #print(menuAdmin)
                        elif opcion == "b" or opcion == "c":
                            os.system("cls")
                            print("En construccion")
                        print(gestionAerolinea)
                        opcion = input("Ingrese opcion: ")
                elif opcion == 2 or opcion == 3 or opcion == 4:
                    print("En construccion")
                opcion = input("Ingrese opcion: ")
    cerrar = False


    
