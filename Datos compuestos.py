#creando una lista (Es modificable)
lista = ["Fresco", "ando ladillado", True, 55]
#creando una tupla (No es modificable)

tupla = ("Fresco", "ando ladillado", True, 55)

lista[3] = "que fastidio"


#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = ("Fresco", "ando ladillado", True, 55)

#crenado un diccionario (dict) (la estructura es key : value y se separamos con comas)
diccionario = {
    "nombre" : "Jeremy Marin",
    "Puesto de trabajo" : "SP2",
    "Sueldo" : 5000,
    "Su pito es grnade?" : True
}

print(diccionario ["Su pito es grnade?"])
