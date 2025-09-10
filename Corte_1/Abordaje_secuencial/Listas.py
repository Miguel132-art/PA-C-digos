#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde', 'Magenta']
#input()
print(my_lista)                                  #imprime la lista
print(type(my_lista))                            #imprime la la tipo de la lista
print(my_lista[2])                               #imprime el tercer elemento de la lista

print("my_lista size: ", len(my_lista))          #el len() se utiliza para obtener la cantidad de elementos de una lista, tupla o diccionario y el print() lo muestra en pantalla
print(my_lista[0:2])                             #imprime desde desde el primer elemento de la lista hasta eñ segundo
print(my_lista[:2])                              #imprime desde desde el primer elemento de la lista hasta eñ segundo

my_lista.append('Blanco')                        #Agrega elemento al final de la lista
print(my_lista)                                  #imprime la lsta actualizada

my_lista.insert(3, 'Negro')                      #agrega en la poscicion 3 el elemento negro
print(my_lista)                                  #imprime lalista actualizada


my_lista.extend(['Marron', 'Gris'])              #Concatena a otra lista
print(my_lista)                                  #imprime la lista actualizada

print(my_lista.index('Azul'))                    #imprime la poscicion en el objeto en la lista

my_lista.remove('Magenta')                       #elimina el elemento Magenta de la lista
my_lista.remove('Marron')                        #elimina el elemento marron de la lista
print(my_lista)                                  #imprime la lista actualizada

my_lista.insert(8, 'Marron')                     #inserta en la poscicion 8 el elemento marron
print(my_lista)                                  #imprime la lista actualizada

print(my_lista.pop())                            #elimina y retorna el ultimo elemento de la lista
size = len(my_lista)                             #la funcion len() obtiene la cantidadad de elementos  dentro de la lista
print("size = ", size)                           #imprime la cantidad de elementos dentro de la lista
print(my_lista.pop())                            #elimina el ultimo elemento de la lista y lo imprime

my_lista_3 = my_lista*3                          #Multiplica x3 todos los elementos de la lista
print("my_lista_3: ", my_lista_3)                #Imprime la lista actualizada

print("Sort:")                                   #Imprime la palabra sort
print()                                          #deja un espacio
my_listaSort = my_lista.sort()                   #ordena la lista por cantidad de caracteres de cada elemento de menor a mayor
print(my_listaSort)                              #No retorna ningun valor ya que la lista se altera en su lugar

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]   #Crea una lista nueva llamada my_NumList
print("Ordering my_NumList: ")                   #Imprime "Ordering my_NumList:"
my_NumList.sort()                                #Ordena la lista de menor a mayor
print(my_NumList)                                #imprime la lista ya ordenada
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)                  #Ahora la ordena de mayor a menor
print("De menor a mayor: ", my_NumList)          #Imprime la lista ahora de mayor a menor



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:



print("============TUPLAS============")                                    
my_tupla = tuple(my_lista)                                                  #Convertir una lista a tupla
print()
print()
print("my_tuple: ", my_tupla)                                               #Muestra la tupla

print(my_tupla[0])                                                          #Muestra el primer elemento dela tupla
print(my_tupla[2])                                                          #Muesta el tercer elemento de la tupla



print('Rojo' in my_tupla)
print(my_tupla.count('Rojo'))                                               #Evalua si un elemento está contenido en la tupla (Devuelve un valor booleano)


my_tupla_unitaria = ('Blanco')                                              #Tupla con un solo elemento
print(my_tupla_unitaria)                                                    #imprime la tupla unitaria


my_tupla = 'Gaspar', 5, 8, 1999                                             #Empaquetado de tupla, tupla sin paréntesis
print(my_tupla)


nombre, dia, mes, año = my_tupla                                            #Desempaquetado de tupla, se guardan los valores en orden de las variables
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)


my_lista2=list(my_tupla)                                                    #Convertir una tupla en una lista
print(my_lista2)