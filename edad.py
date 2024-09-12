import os
import platform
import time
 
delay = 2
 

def validar_edad(a:int):
    if a >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
    time.sleep(delay)
   
def salir():
    print("Gracias por utilizar el sistema.")
   

def f_repetir(): #entrega falso o verdadero
    opcion = input("Si desea volver al menú ingrese [m], de lo contrario, presione cualquier tecla: ")    
    if opcion.lower() == "s":
        limpiar_consola()
   
        return True
    else:
        limpiar_consola()
        return False
   
#para limpiar la consola
def limpiar_consola():
    sistema = platform.system() #platform captura el sistema enel que se trabaj
   
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")
 
def validar_entero(): #entrega 
   
    edad = int(input("Ingrese la edad a validar: "))
    limpiar_consola()
    try:
        if edad == int:
            limpiar_consola()
    except ValueError:
        print("Error ingrese un entero")
    validar_edad(edad)
    
 
 
def main():
    repetir = True
    while repetir: #repite hasta que sea falso
        validar_entero()
        repetir = f_repetir()
       
    salir()
   
main()
   
 
 
