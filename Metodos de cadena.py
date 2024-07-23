cadena1 = "Te pica el culo?"
cadena2 = "mmgvo"
cadena3= "54822368496"
cadena4 = "Cuidatelasnalgas"

#convierte el texto en mayuscula
resultado = cadena1.upper()

#convierte el texto en miniscula
resultado2 = cadena1.lower() 

#primera letra en mayuscula
resultado3 = cadena2.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1
resultado4 = cadena1.find("culo")

#buscamos una cadena en otra cadena, si no hay coincidencia lanza una exepcion
resultado5 = cadena1.index("T")

#si es numerico devolvemos true, sino devolvemos false
resultado6 = cadena3.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos false
resultado7 = cadena4.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
resultado8 = cadena4.count("a")

#contamos cuantos caracteres  tiene una cadena
resultado9 = len(cadena4)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
resultado10 = cadena1.startswith("Te")

##verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
resultado11 = cadena1.endswith("?")

#rempalza un pedazo de la cadena dada, por otra dada. Si el valor 1, se encuentra en la cadena original, remplazara el valor de 1 de la misma, por el valor 2
resultado12 = cadena2.replace("mmgvo" , "becerro")

#separar cadenas con la cadena que le pasemos
resultado13 = cadena1.split(",")



print (resultado13 [0])