# Tublas
tupla1 = ()# defina una tupla vacia
print(tupla1)

tupla2 = ("una cadena ",123,4.9,True)#una tupla heterogenia
print(tupla2)
print(tupla2[1])#acceder al elemento de la tupla
print(tupla2[2])

tupla3 = (0,1,2,3)
tupla4 = ("A","B","C")
tupla5 = (tupla3,tupla4)
print(tupla5)
print(tupla5[1][1]) #muestra  de la tuplas2 el elemento en el indece 1
print(tupla5[1][0])
print(tupla5[0][3])

#operaciones con las tuplas
tupla6 = ("A","B","C","D","E")
tupla7 = (1,2,3,4,5)
tupla8 = tupla6 + tupla7 # concatenar
print(tupla8[8])
print(tupla8)

#repetir  una tupla
tupla9 = (1,2,3,4,5)
tupla10 = tupla9 *3
print(tupla10)


# compar una tupla
tupla11 = ("rojas",)
tupla12 = (123,)
tupla13 = ("rosas",)
tupla14 = ("Rosas",)
 print((tupla11,tupla12)< (tupla13,tupla14))
 print((tupla15,tupla14)==(tupla16,tupla14))


#Definicion de una lista
lista= []#lista vacia
listal = ["Este es un texto"] #Una lista con un elemento.
lista2 = ['Una cadena', 123] #Una lista de dos elementos
lista3 = [1, 2,3,4.5, 'hola', 'a'] #Una lista de seis elementos
 print(lista)
 print(listal)
 print(lista2)
 print(lista3)

#listas enlazadas
 lista5 =[0,1,2,3]
 lista6 =["A", "B", "C"]
 lista7 = [lista5, lista6]
 print (lista7)
 print(lista7 [0]) #Muestra sola listas
 print(lista7 [1]) #Muestra sola lista6
 print (lista7 [1][0]) #Muestra de la lista6 el elemento en el indice 0


