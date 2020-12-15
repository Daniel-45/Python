# Programacion orientada a objetos

# Definir una clase - molde para crear objetos de ese tipo
class Coche:

    # Atributos - caracteristicas del objeto
    # Doble guión bajo para atributos privados
    __marca = ''
    __modelo = ''
    __color = ''
    __cv = 0
    __velocidad = 0
    __plazas = 0
    __puertas = 0

    # Constructor
    def __init__(self, marca, modelo, color, cv, velocidad, plazas, puertas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cv = cv
        self.velocidad = velocidad
        self.plazas = plazas
        self.puertas = puertas

    # Metodos - acciones que realiza el objeto
    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getCv(self):
        return self.cv

    def setCv(self, cv):
        self.cv = cv

    def getVelocidad(self):
        return self.velocidad

    def acelerar(self):
        self.velocidad += 6

    def frenar(self):
        self.velocidad -= 6

    def getPlazas(self):
        return self.plazas

    def setPlazas(self, plazas):
        self.plazas = plazas

    def getPuertas(self):
        return self.puertas

    def setPuertas(self, puertas):
        self.puertas = puertas

    def mostrarDatos(self):
        info = '\n------ Informacion del coche ------'
        info += '\nMarca: ' + self.getMarca()
        info += '\nModelo: ' + self.getModelo()
        info += '\nColor: ' + self.getColor()
        info += '\nCV: ' + str(self.getCv())
        info += '\nVelocidad: ' + str(self.getVelocidad())
        info += '\nPlazas: ' + str(self.getPlazas())
        info += '\nPuertas: ' + str(self.getPuertas())

        return info

# Final definicion de la clase