
palabras = ["perro", "gato", "elefante", "oso", "jirafa, leon, cocodirlo"]
palabrasLargas = list(filter(lambda palabra: len(palabra) > 5, palabras))
print(palabrasLargas)
