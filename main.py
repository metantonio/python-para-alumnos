saludo = "saludo"
numero = 1.5
boleano = False
lista1 = [saludo, numero, boleano]
tupla1 = (saludo, numero, boleano)
lista1[2] = "indice 2"
#tupla1[2] = "indice 2" ##no se puede hacer con tuplas
diccionario = {
    "propiedad1": "hola",
    "propiedad2": "Mundo"
}

diccionario["propiedad2"]="Jack"
#print(lista1)
#print(tupla1)
#print(diccionario)


def bucleFor():
    for item in lista1:
        print(item)
    return

def bucleFor2():
    for i in range(5, 10):
        print(i)
    return



#bucleFor()
#bucleFor2()
#entradaUsuario = input("\n Coloque un número \n") ##esto dará error porque es un string a la hora de sumar
#entradaUsuario = int(input("\n Coloque un número \n"))

#print("Resultado: ",entradaUsuario+7)

print("""\n Menú Principal
    Menú:

    1-. Ver Reservaciones
    2-. Realizar una Reservacion
    3-. Borrar una Reservacion
    4-. Salir

    """)

""" opcionUsuario = int(input("\n Elige una opción del menú principal"))

while opcionUsuario<4:
    if(opcionUsuario==1):
        print("ver reservarciones \n")
        opcionUsuario = int(input("\n Elige una opción del menú principal \n"))
    if(opcionUsuario==2):
        print("se realiza una reservacion \n")
        opcionUsuario = int(input("\n Elige una opción del menú principal \n"))
    if(opcionUsuario==3):
        print("Se borra la reservación \n")
        opcionUsuario = int(input("\n Elige una opción del menú principal \n"))
    if(opcionUsuario>=4):
        break """


class Reservaciones:
    def __init__(self, nombre, fecha, evento):
        self.nombre = nombre
        self.fecha = fecha
        self.evento = evento
    
    def serialize(self):
        return {
            "nombre": self.nombre,
            "fecha": self.fecha,
            "evento":self.evento
        }

class Aulas(Reservaciones):
    def __init__(self, identificacion, capacidad, aulaSencilla, nombre, fecha, evento):
        self.identificacion = identificacion
        self.capacidad = capacidad
        self.aulaSencilla = aulaSencilla
        super().__init__(nombre, fecha, evento)

    def serialize(self):
        return {
            'identificacion': self.identificacion,
            'capacidad': self.capacidad,
            'aulaSencilla': self.aulaSencilla,
            'nombre': self.nombre,
            'fecha': self.fecha,
            'evento': self.evento
        }

    @classmethod
    def registrar(cls, identificacion, capacidad, aulaSencilla, nombre, fecha, evento):
        nueva_aula = cls(
            identificacion,
            capacidad,
            aulaSencilla,
            nombre,
            fecha,
            evento
        )
        return nueva_aula

    


if __name__ == '__main__':
    #reservacion_concierto = Reservaciones("Antonio", "6-05-2022", "Concierto Cold Play")
    #print(reservacion_concierto.serialize())
    reservacion1= Aulas("Aula001", 50, True, "Jose Manuel", "6-05-2022", "Exposición")
    #print(reservacion1.serialize())
    reservacion2 = Aulas.registrar("Aula002", 20, False, "Luis", "6-05-2022", "Laboratorio")
    print(reservacion2.serialize())
 