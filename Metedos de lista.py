#creando una lista con list
lista = list(["ingenio" , "brutalidad" , "dinero" , 4656])
lista2 = list([523256 , 44 , 22, 5 , 59746 , 5413 , 1 , 0])
#devulve la cantida de elementos que se encuentran en una lista
resultado = len(lista)

#agregando un elemento a la lista
lista.append("lastima")

#agregando un elemento a la lista en un indice especifico
lista.insert(2 , "riqueza")

#agregando varios elementos a la lista
lista.extend([True , "grandeza" , 65894])
lista2.extend([True , False , False])
#eliminado un elemento de la lista por su indice
lista.pop(4) #-1 para eliminar el ultimo, -2 para eliminar el antepenultimo y asi sucesivamente

#removiendo un elemento de la lista por su valor 
lista.remove(65894)

#ordenadno la lista de forma ascendente (si usamos el parameto reverse=True lo ordena en reversa )
lista2.sort()

#invirtiendo los elementos de una lista 
lista.reverse()

#verificnado si un elemento se encuentra en la lista
encontrar = lista2.index(0)

#eliminando todos los elementos de la lista
lista.clear()

print (encontrar)