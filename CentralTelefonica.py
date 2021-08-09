import random
import pyglet
import time
import os
import pandas as pd

class CentralTelefonica: 

    #Variables
    abonados = [] 
    duracionLlamadas = 0

    #Inicializadores
    def __init__(self):
        self.inicializarNumeros()

    def inicializarNumeros(self):
        for i in range(20):
            numero = random.randint(3000000000, 3200000000)
            nuevoAbonado = Telefono(numero, i)
            self.abonados.append(nuevoAbonado)

    #Funciones
    def aumentarDuracionLlamada(self, nuevaDuracion):
        self.duracionLlamadas += nuevaDuracion

    def precioAPagar(self):
        resultado = "%i$" %(self.duracionLlamadas * 10) #Se cobra el segundo a 10 pesos
        return resultado

class Telefono:

    #Variables
    numero = ""
    estado = ""
    tono = ""
    duracionLlamada = 0
    posiblesEstados = ["Fuera de servicio", "Ocupado", "Disponible"]

    #Inicializadores
    def __init__(self, numero, estado):

        self.estado = estado
        self.numero = numero
        self.inicializarEstado()
    
    def inicializarEstado(self):

        if int(self.estado) <= 2:
            self.estado = self.posiblesEstados[0]
        elif int(self.estado) > 2 and self.estado <= 7:
            self.estado = self.posiblesEstados[1]
        else:
            self.estado = self.posiblesEstados[2] 

    #Funciones
    def inicializarTono(self):

        player = pyglet.media.Player()
        if self.estado == self.posiblesEstados[0]:
            self.tono = pyglet.resource.media("tonoFueradeServicio.mp3", streaming= False)
            player.queue(self.tono)

        elif self.estado == self.posiblesEstados[1]:
            self.tono = pyglet.resource.media("tonoOcupado.wav", streaming= False)
            player.queue(self.tono)

        else:
            self.tono = pyglet.resource.media("tonoMarcando.wav", streaming= False)
            player.queue(self.tono)
            player.play()
            time.sleep(7)
            randomAnswer = random.randint(1,3)
            print(randomAnswer)
            player.next_source()

            if randomAnswer == 1:
                self.tono = pyglet.resource.media("conversacion1.wav", streaming= False)
                self.duracionLlamada = int(self.tono.duration)
                player.queue(self.tono)

            elif randomAnswer == 2:
                self.tono = pyglet.resource.media("conversacion2.mp3", streaming= False)
                self.duracionLlamada = int(self.tono.duration)
                player.queue(self.tono)

            else:
                self.tono = pyglet.resource.media("conversacion3.wav", streaming= False)
                self.duracionLlamada = int(self.tono.duration)
                player.queue(self.tono)

        player.play()
        time.sleep(self.tono.duration)
        player.next_source()
        
os.system('cls') 


programaCondicion = True #Condicion con la cual el while funciona el programa no correria sin esta
print("Muy buenas tardes, habla Juan David. En que puedo ayudarlo hoy?")
time.sleep(2)
print(
'''
Elija una de las siguientes opciones:
    
    1) Llamar a un abonado.
    2) "Nada, me confundi"
Por favor digite alguna de las opciones o presione cualquier otro boton para salir
'''
)
opcionRespuesta = int(input())

os.system('pause')
os.system('cls') 

central = CentralTelefonica()

while programaCondicion:

    if opcionRespuesta == 1:
        print("A cual numero deseas llamar? Los numeros son los siguientes: ")

        #Los numero son mostrados al usuario
        for i in range(20):
            print("%i) numero: %i estado: %s" %(i + 1, central.abonados[i].numero, central.abonados[i].estado))
        df = pd.DataFrame(data = central.abonados, columns= "Numeros")
        df.to_excel()
        numeroSeleccionado = int(input())
        print("seleccionaste el numero %i" %(central.abonados[numeroSeleccionado - 1].numero))
        print("Llamar al numero? y = si")
        llamar = str(input())

        if llamar == "y":
            central.abonados[numeroSeleccionado - 1].inicializarTono()
            central.aumentarDuracionLlamada(central.abonados[numeroSeleccionado - 1].duracionLlamada)

        os.system('pause')
        os.system('cls') 
        
        #Revisa el estado del abonado seleccionado y muestra de acuerdo a este. 
        if central.abonados[numeroSeleccionado - 1].estado == "Fuera de servicio" :
            print("Lo sentimos, el numero marcado no se encuentra en servicio.")

        elif central.abonados[numeroSeleccionado - 1].estado == "Ocupado" :
            print("El numero marcado se encuentra ocupado, intente luego.")

        elif central.abonados[numeroSeleccionado - 1].estado == "Disponible":
            print("Llamada exitosa")
            print("Duracion de la llamada: %is " %central.duracionLlamadas)

    print("Le gustaria llamar de nuevo? y = si")
    reiniciar = str(input())
    if reiniciar != "y":
        programaCondicion = False

    if opcionRespuesta == 2:
        programaCondicion = False

#Llamar funcion precio, esta va a devolver el string creado en la central, los segundos multiplicados por el precio.
print("Precio a pagar: %s" %central.precioAPagar())
    
