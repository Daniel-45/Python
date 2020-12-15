import clases

persona = clases.Persona('Emma', 'Ciambrino Baz', 38, 1.58, 53)

print(persona.mostrarDatos())
print(persona.hablar())

informatico = clases.Informatico('Daniel', 'Pompa Pareja', 46, 1.78, 78, 'Java, JavaScript, Python, HTML5, CSS3', 1)

print(informatico.mostrarDatos())
print(f'Lenguajes: {informatico.getLenguajes()}')
print(informatico.programar())