# JUEGO PIEDRA PAPEL O TIJERA
#el juego consiste en que la pc y el jugador tomaran una de las tres opciones.
#y el programa determinará quien de los dos ganó o quien perdio o si hubo empate
#el juego permite jugar las veces que el jugador desee o hasta que lo finelice.

import random #esto es para que la libreria se importe y pueda ser utilizada
import time #permite manejar timpo
from time import sleep#para ser mas especifico para que se tome una pausa para hacer el
#juego mas real como que la computadora esta pensando para ver que elije y ver quien de los dos gano
def eleccion_computadora():#no tiene parametro asique no necesita ningun dato dentro de los ()
#estamos def la función que elejimos mas abajo  
    numero_random=random.randint(0,2)#significa que va a elegir un numero entero entre 0 y 2
#0,2 quiere decir que hay 3 opciones y se cuenta del 0 1 2
    opciones=["PIEDRA", "PAPEL", "TIJERAS"]
#piedra, papel y tijeras son mis 3 opciones
    x=opciones[numero_random] #guardamos en una variable en este caso es x es igual a opciones pero quien elije es numero ramdon
#es decir si se obtiene el numero 0 tomara piedra, si al generar el numero ramdon 1 tomara pepel si el n 2 tomara tijera  
    return x
#retornamos x


# https://docs.python.org/es/3/library/random.html 


#para crear las funciones necesitamos dos librerias de random y time
#la libreria en random permite crear un numero aletorio
#crearemos dos funciónes obtener resultados, eleccion_computadora
def obtenerResultados(eleccion_pc,eleccion_jugador):
    if(eleccion_pc==eleccion_jugador):
#si la eleccion de la pc es igual al jugador
        print("\t\t\t :-v Esto es un empate :-v")
#impimira esto es un empate
    elif(eleccion_pc=="PIEDRA" and eleccion_jugador=="TIJERAS"):
#si la eleccion de la pc piedra y el jugador tijera
        print("\t\t\t :-( Perdiste :-(")
#imprimira que perdi
    elif(eleccion_pc=="PAPEL" and eleccion_jugador=="PIEDRA"): 
        print("\t\t\t :-( Perdiste :-(")
    elif(eleccion_pc=="TIJERAS" and eleccion_jugador=="PAPEL"):
        print("\t\t\t :-( Perdiste :-(")
    elif(eleccion_pc=="PIEDRA" and eleccion_jugador=="PAPEL"):
        print("\t\t\t :-) Ganaste :-)")
    elif(eleccion_pc=="PAPEL" and eleccion_jugador=="TIJERAS"):
        print("\t\t\t :-) Ganaste :-)")
    elif(eleccion_pc=="TIJERAS" and eleccion_jugador=="PIEDRA"):
        print("\t\t\t :-) Ganaste :-)")

print("\tJUEGO PIEDRA PAPEL O TIJERAS\n Intenta ganar las veces que quieras!!")
x="s"
while x!="n" and x!="N":
#x(!))es distinto o diferente a la letra n o N es decir para que se lean de las dos formas
    print("Elija una opcion\nPiedra \nPapel \nTijeras")
#estamos imprimiendo una opción
    eleccion_jugador=input("\tElija una opción->").upper() 
#upeer esto hara que la persona lo que elija sin importar si lo escribio con mayuscula y minuscula 
#le damos un imput para elegir a un jugador 
    if(eleccion_jugador!="PIEDRA" and eleccion_jugador!="PAPEL" and eleccion_jugador!="TIJERAS"):
#si la eleccion del jugador es diferente a piedra y tambien es diferente a papel, tijeras
      print("\tEsta opción no existe, vuelva a intentar.")
#aqui esta imprimiendo un error con la finelidad de que el usuario o jugador sepa que no elijio unade las 3 opciones p,p,t
    else:
#aqui le estamos diciendo que si elije una de las opción le dara elresultado sin problemas
        print("\t\tTu eleccion fue: \t", eleccion_jugador)
#aqui estamos imprimiendo lo que la persona elijio
        sleep(0.9) #sleep es para darle un tiempo cuando se ejecute
        eleccion_pc=eleccion_computadora()
        print("\t\tLa computadora elijió: \t", eleccion_pc)
#aqui estamos mostrando lo que la computadora eligio:
        sleep(0.9)#sleep es darle un tiempo
        obtenerResultados(eleccion_pc,eleccion_jugador)
#hacemos uso de la función obtenerResultados esto va a funcionar con la función pc y jugador
    x=input("Quieres continuar \ns/n\n->")
#estamos preguntando si quiere o no continuar 

print("\t\t ¡GRACIAS POR JUGAR!")
# le decimos gracias por jugar
K=input()#me permite hacer una pausa


    

    
    


