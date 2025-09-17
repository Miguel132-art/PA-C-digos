# Diccionario con sensores de diferentes habitaciones y temperaturas
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# Diccionario con el número de cámaras en diferentes ubicaciones
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

# Imprime los diccionarios de sensores y cámaras
print(sensors)
print(num_cameras)

# Diccionario con traducciones de palabras de inglés a otro idioma
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
# Imprime las traducciones
print(translations)

# Verificación de un error en el siguiente diccionario (listas como claves, lo cual es inválido en Python)
#powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# Esto lanzará un error porque las listas no pueden ser claves en un diccionario
#print(powers)

# Diccionario con listas de hijos
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
# Imprime el diccionario con los nombres de los hijos
print(children)

# Diccionario vacío
my_empty_dictionary = {}
# Imprime el diccionario vacío
print(my_empty_dictionary)

# Diccionario de menú con precios de alimentos
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# Imprime el menú antes de agregar el "cheesecake"
print("Before: ", menu)
# Agrega el "cheesecake" al menú con su precio
menu["cheesecake"] = 8
# Imprime el menú después de agregar el "cheesecake"
print("After", menu)

# Actualiza el diccionario de animales en el zoológico
animals_in_zoo = {"dinosaurs": 0}
# Se reemplaza el valor anterior con el número de caballos
animals_in_zoo = {"horses": 2}
# Imprime el diccionario con el número de caballos
print(animals_in_zoo)


## Agregar múltiples claves al diccionario de sensores
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
# Imprime el diccionario antes de agregar nuevas habitaciones
print("Before", sensors)

# Si se quisieran agregar tres habitaciones nuevas, se usaría update():
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
# Imprime el diccionario después de agregar las nuevas habitaciones
print("After", sensors)

### Agregar usuarios con sus IDs
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
# Imprime el diccionario de IDs antes de actualizarlo
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
# Imprime el diccionario de IDs después de agregar nuevos usuarios
print(user_ids)

## Sobrescribir valores de claves en un diccionario
# Agrega un nuevo ítem al menú con la clave "banana"
menu["banana"] = 3
# Reinicia el diccionario del menú a su estado inicial
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
# Imprime el menú antes de sobrescribir el valor de "oatmeal"
print("Before: ", menu)
# Modifica el valor de "oatmeal"
menu["oatmeal"] = 5
# Imprime el menú después de la modificación
print("After", menu)

# Se observa que el valor de "oatmeal" ha cambiado de 3 a 5.

# Diccionario con ganadores de los premios Oscar
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
# Imprime los ganadores antes de actualizarlos
print("Before", oscar_winners)
print()
# Agrega la categoría de "Supporting Actress" al diccionario
oscar_winners.update({"Supporting Actress": "Viola Davis"})
# Imprime el diccionario después de agregar la nueva categoría
print("After1", oscar_winners)
print()
# Modifica el valor de "Best Picture"
oscar_winners["Best Picture"] = "Moonlight"
# Imprime el diccionario después de la modificación
print("After2", oscar_winners)


### Diccionarios por comprensión (dict comprehension)
# Combina dos listas en un diccionario usando dict comprehension

# Listas de nombres de estudiantes y sus alturas
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# zip() combina las dos listas en un iterador de tuplas, cada una con un nombre y una altura
zipStudents = zip(names, heights)
# Imprime el objeto zip (es un iterador)
print("zipStudents: ", zipStudents)

# Usando dict comprehension para crear un diccionario de estudiantes con sus alturas
students = {key:value for key, value in zip(names, heights)}
# Imprime el diccionario de estudiantes
print(students)

# Zip para combinar listas de bebidas y su contenido de cafeína
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
# Imprime el objeto zip de bebidas y cafeína
print(zipped_drinks)

# Crear un diccionario con bebidas y su cafeína usando dict comprehension
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
# Imprime el diccionario de bebidas y cafeína
print(drinks_to_caffeine)

# Listas de canciones y sus respectivos números de reproducciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
# Crear un diccionario de canciones y reproducciones con dict comprehension
plays = {key:value for key, value in zip(songs, playcounts)}
# Imprime el diccionario de canciones y reproducciones
print(plays)
# Actualiza el diccionario con nuevas reproducciones
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
# Imprime el diccionario después de las actualizaciones
print("After: ", plays)

# Crea un diccionario de bibliotecas con un conjunto de canciones
library = {"The Best Songs": plays, "Sunday Feelings": {}}
# Imprime el diccionario de bibliotecas
print(library)

