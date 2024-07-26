diccionario = {
    "nacionalidad" : "Venezolana" ,
    "edad" : 19 ,
    "eres hombre?" : True
}

#nos devuwelve un objeto dict_item (dict_item es un objeto que se puede iterar)
llaves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor = diccionario.get("edad")

#eliminando un elemento del diccionario
diccionario.pop("edad")

#eliminando todo del diccionario
diccionario.clear()

print(diccionario)