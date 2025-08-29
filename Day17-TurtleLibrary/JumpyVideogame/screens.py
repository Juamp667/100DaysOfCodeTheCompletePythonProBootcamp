import os

# Carpeta donde están los archivos
folder = r"C:\Users\Juamp6.67\Documents\projects\100DaysOfCodeTheCompletePythonProBootcamp\Day17-TurtleLibrary\myImplementation\images\winnerScreen"

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isfile(file_path):
        name, ext = os.path.splitext(filename)

        # Suprime las últimas 4 letras del nombre
        if len(name) > 12:  
            new_name = name[:-12] + ext
        else:
            new_name = name + ext  # si tiene menos de 4 letras, lo deja igual

        new_path = os.path.join(folder, new_name)

        os.rename(file_path, new_path)
        print(f"Renombrado: {filename} -> {new_name}")