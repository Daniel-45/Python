'''
Herencia
Permite compartir atributos y métodos entre clases.
Existe una clase padre de la que pueden heredar otras clases.
'''

# Clase padre
class Persona:
    """
    nombre = ''
    apellidos = ''
    edad = 0
    altura = 0
    peso = 0
    """

    def __init__(self, nombre, apellidos, edad, altura, peso):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellidos(self):
        return self.apellidos 

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getEdad(self):
        return self.edad 
    
    def setEdad(self, edad):
        self.edad  = edad

    def getAltura(self):
        return self.altura 

    def setAltura(self, altura):
        self.altura = altura

    def getPeso(self):
        return self.peso 

    def setPeso(self, peso):
        self.peso = peso
    
    def hablar(self):
        return 'Estoy hablando'

    def caminar(self):
        return 'Estoy caminando'

    def comer(self):
        return 'Estoy comiendo'

    def dormir(self):
        return 'Estoy durmiendo'

    def mostrarDatos(self):
        info = '\n---------- Información ----------'
        info += '\nNombre: ' + self.getNombre()
        info += '\nApellidos: ' + self.getApellidos()
        info += '\nEdad: ' + str(self.getEdad())
        info += '\nAltura: ' + str(self.getAltura())
        info += '\nPeso: ' + str(self.getPeso())

        return info


# Clase hija
class Informatico(Persona):

    """
    lenguajes = ''
    experiencia = 0
    """

    def __init__(self, nombre, apellidos, edad, altura, peso, lenguajes, experiencia):
        super().__init__(nombre, apellidos, edad, altura, peso)
        self.lenguajes = lenguajes
        self.experiencia = experiencia

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def getExperiencia(self):
        return self.experiencia

    def setExperiencia(self, experiencia):
        self.experiencia = experiencia

    def programar(self):
        return 'Estoy programando'

    def repararPC(self):
        return 'He reparado el PC'

