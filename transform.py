def eliminarPrimerasLineas(archivo, eliminar):
    with open(archivo, "r") as f:
        lineas = f.readlines()[eliminar:]
    with open(archivo, "w") as f:
        f.writelines(lineas)

def eliminarLineasConteniendo(archivo, eliminar):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    lineasFiltradas = [linea for linea in lineas if eliminar not in linea]

    with open(archivo, "w") as f:
        f.writelines(lineasFiltradas)

def eliminarPalabraEnLineas(archivo, palabraAEliminar):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    lineasModificadas = [linea.replace(palabraAEliminar, "") for linea in lineas]

    with open(archivo, "w") as f:
        f.writelines(lineasModificadas)

def eliminarEspaciosEnBlancosYAgregarPuntoComa(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    lineasModificadas = [linea.replace(" ", ";") for linea in lineas]

    with open(archivo, "w") as f:
        f.writelines(lineasModificadas)

def eliminarPuntoComaDuplicados(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    lineasModificadas = [linea.replace(";;", ";") for linea in lineas]
    with open(archivo, "w") as f:
        f.writelines(lineasModificadas)

def reemplazarTexto(archivo, textoABuscar, textoAReemplazar):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    lineasModificadas = [linea.replace(textoABuscar, textoAReemplazar) for linea in lineas]
    with open(archivo, "w") as f:
        f.writelines(lineasModificadas)

archivo = "Registro.txt"

eliminarPrimerasLineas(archivo, 6)
eliminarLineasConteniendo(archivo, "Index: []")
eliminarLineasConteniendo(archivo, "Columns: [xmin, ymin, xmax, ymax, confidence, class, name]")
eliminarLineasConteniendo(archivo, "Empty DataFrame")
eliminarPalabraEnLineas(archivo, "xmin")
eliminarPalabraEnLineas(archivo, "ymin")
eliminarPalabraEnLineas(archivo, "xmax")
eliminarPalabraEnLineas(archivo, "ymax")
eliminarPalabraEnLineas(archivo, "confidence")
eliminarPalabraEnLineas(archivo, "class")
eliminarPalabraEnLineas(archivo, "name")
eliminarPalabraEnLineas(archivo, ";")
eliminarEspaciosEnBlancosYAgregarPuntoComa(archivo)
eliminarPuntoComaDuplicados(archivo)
reemplazarTexto(archivo, "classignore", "class_ignore")
reemplazarTexto(archivo, "EmptyDataFrame", "Empty DataFrame")

print(f"Se han realizado todas las operaciones en el archivo {archivo}")
