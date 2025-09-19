# Diccionario con alturas de edificios más altos del mundo
building_heights = {
    "Burj Khalifa": 828, 
    "Shanghai Tower": 632, 
    "Abraj Al Bait": 601, 
    "Ping An": 599, 
    "Lotte World Tower": 554.5, 
    "One World Trade": 541.3
}

# Imprime la altura del Burj Khalifa
print(building_heights["Burj Khalifa"])

# Imprime la altura del Ping An junto con su nombre
print("Ping An", building_heights["Ping An"])

# Diccionario con elementos del zodiaco clasificados por sus elementos
zodiac_elements ={
    "water": ["Cancer", "Scorpio", "Pisces"], 
    "fire": ["Aries", "Leo", "Sagittarius"], 
    "earth": ["Taurus", "Virgo", "Capricorn"], 
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Imprime los signos zodiacales de tierra
print(zodiac_elements["earth"])

# Imprime los signos zodiacales de fuego
print(zodiac_elements["fire"])

# Se añade un nuevo edificio "Landmark" con altura de 81 metros al diccionario
building_heights = {
    "Burj Khalifa": 828, 
    "Shanghai Tower": 632, 
    "Abraj Al Bait": 601, 
    "Ping An": 599, 
    "Lotte World Tower": 554.5, 
    "One World Trade": 541.3, 
    "Landmark": 81 
}

# Imprime la altura del Landmark
print(building_heights["Landmark"])

# Verifica si la clave "Landmark 81" está en el diccionario
key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights["Landmark 81"])  # No se ejecutará, ya que "Landmark 81" no existe, sino "Landmark"

# Añadir una clave no zodiacal "energy"
zodiac_elements["energy"] = "Not a Zodiac element"

# Verifica si "energy" está en el diccionario y la imprime
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])

# Usamos el método `get()` para obtener la altura del Shanghai Tower
building_heights = {
    "Burj Khalifa": 828, 
    "Shanghai Tower": 632, 
    "Abraj Al Bait": 601, 
    "Ping An": 599, 
    "Lotte World Tower": 554.5, 
    "One World Trade": 541.3
}

# Usamos `get()` para obtener la altura de Shanghai Tower, si no existe devuelve None (sin error)
building_heights.get("Shanghai Tower")

# Usamos `get()` para obtener un valor que no existe (no genera error, devuelve None)
building_heights.get("My House")

# Diccionario de IDs de usuario
user_ids = {
    "teraCoder": 100019, 
    "pythonGuy": 182921, 
    "samTheJavaMaam": 123112, 
    "lyleLoop": 102931, 
    "keysmithKeith": 129384
}

# Intenta obtener el ID de "teraCoder", si no existe asigna un valor por defecto
user_ids.get("teraCoder")

# Si el ID de "teraCoder" es None, asigna un valor por defecto (1000)
if user_ids.get("teraCoder") == None:
    tc_id = 1000
else: 
    tc_id = user_ids.get("teraCoder")

# Imprime el valor del ID de "teraCoder"
print(tc_id)

# Si "superStackSmash" no existe en el diccionario, asigna un valor por defecto a stack_id
if user_ids.get("superStackSmash") == None:
    stack_id = 100000

# Imprime el valor de stack_id (100000 si no existía "superStackSmash")
print(stack_id)

# Diccionario de premios de una rifa
raffle = {
    223842: "Teddy Bear", 
    872921: "Concert Tickets", 
    320291: "Gift Basket", 
    412123: "Necklace", 
    298787: "Pasta Maker"
}

# El método pop() elimina el ítem con la clave indicada y lo imprime, si no existe se imprime el valor por defecto
print(raffle.pop(320291, "No Prize"))

# Imprime el estado actual del diccionario raffle (sin el ítem 320291)
print(raffle)

# Intenta eliminar un ítem con una clave inexistente (imprime el valor por defecto "No Prize")
print(raffle.pop(100000, "No Prize"))

# Imprime el estado actualizado del diccionario raffle
print(raffle)

# Elimina otro ítem (872921) y lo imprime
print(raffle.pop(872921, "No Prize"))

# Imprime el estado final del diccionario raffle
print(raffle)

# Diccionario con cantidad de objetos disponibles
available_items = {
    "health potion": 10, 
    "cake of the cure": 5, 
    "green elixir": 20, 
    "strength sandwich": 25, 
    "stamina grains": 15, 
    "power stew": 30
}

# Inicializa la cantidad de puntos de salud
health_points = 20

# Se agregan los valores de ciertos objetos al total de puntos de salud (pop elimina el objeto del diccionario)
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)  # "mystic bread" no existe, por lo que suma 0

# Imprime el estado actual del diccionario de objetos y la cantidad final de puntos de salud
print(available_items)
print(health_points)

# Diccionario con las puntuaciones de varios estudiantes
test_scores = {
    "Grace": [80, 72, 90], 
    "Jeffrey": [88, 68, 81], 
    "Sylvia": [80, 82, 84], 
    "Pedro": [98, 96, 95], 
    "Martin": [78, 80, 78], 
    "Dina": [64, 60, 75]
}

# Imprime las claves del diccionario, es decir, los nombres de los estudiantes
print(list(test_scores))

# Itera sobre las claves (nombres de los estudiantes) y las imprime
for student in test_scores.keys():
    print(student)

# Diccionarios de usuarios y lecciones con sus cantidades
user_ids = {
    "teraCoder": 100019, 
    "pythonGuy": 182921, 
    "samTheJavaMaam": 123112, 
    "lyleLoop": 102931, 
    "keysmithKeith": 129384
}

num_exercises = {
    "functions": 10, 
    "syntax": 13, 
    "control flow": 15, 
    "loops": 22, 
    "lists": 19, 
    "classes": 18, 
    "dictionaries": 18
}

# Obtiene las claves (nombres de usuarios y lecciones) y las imprime
users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)

# Itera sobre los valores de las puntuaciones de los estudiantes y los imprime
for score_list in test_scores.values():
    print(score_list)

# Calcula el total de ejercicios sumando los valores de num_exercises
total_exercises = 0
for exercises in num_exercises.values():
   total_exercises += exercises

# Imprime el total de ejercicios
print(total_exercises)

# Diccionario con el valor de las marcas más grandes
biggest_brands = {
    "Apple": 184, 
    "Google": 141.7, 
    "Microsoft": 80, 
    "Coca-Cola": 69.7, 
    "Amazon": 64.8
}

# Itera sobre los elementos (marca y valor) y los imprime
for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")

# Diccionario con el porcentaje de mujeres en diversas ocupaciones
pct_women_in_occupation = {
    "CEO": 28, 
    "Engineering Manager": 9, 
    "Pharmacist": 58, 
    "Physician": 40, 
    "Lawyer": 37, 
    "Aerospace Engineer": 9
}

# Itera sobre las ocupaciones y los porcentajes y los imprime
for occupation, percentage in pct_women_in_occupation.items():

    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
