
"""
Los Beatles fue un grupo musical muy famoso que fue cambiando a lo largo de los años,
entraron y salieron muchos de sus componentes. 
Vamos a representar estos cambios con un programa que nos permita practicar el concepto de lista.
1.Crea una lista llamada beatles
2.Añade los miembros de la banda John, Paul, George.
3.Añade los siguientes miembros de la banda, Stu y Pte.
4.Elimina a Stu y Pete.
5.Agrega a Ringo.
"""

beatles = ["Jonh, Paul, George"]

print(beatles)

beatles.append("Stu")
beatles.append("Pete")

print(beatles)

beatles.remove("Stu")
beatles.remove("Pete")

beatles.insert(3,"Ringo")

print(beatles)
