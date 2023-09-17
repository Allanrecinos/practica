# Definir la lista de alumnos y sus notas
datos_alumnos = [
    "Juan,98,87,89,90",
    "Jose,90,43,20,40",
    "Pedro,70,80,89,90"
]

# Crear un diccionario para almacenar el promedio de las notas de cada estudiante
promedios = {}

# Calcular el promedio de las notas para cada estudiante
for alumno in datos_alumnos:
    partes = alumno.split(',')
    nombre = partes[0]
    notas = [int(x) for x in partes[1:]]
    promedio = sum(notas) / len(notas)
    promedios[nombre] = promedio

# Guardar los promedios en un archivo de texto
with open("promedios.txt", "w") as archivo:
    for nombre, promedio in promedios.items():
        archivo.write(f"{nombre}={promedio:.2f}\n")

print("Promedios guardados en el archivo 'promedios.txt'")