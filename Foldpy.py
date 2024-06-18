from pathlib import Path
import send2trash
import shutil
import glob
import os


def mostrar_carpetas(ruta):
    ruta_ = Path(ruta)
    lista_carpetas = []
    contador = 1
    for carpeta in ruta_.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_carpetas.append(carpeta)
        contador += 1
    return lista_carpetas


def elegir_(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input('\nElige una opcion: ')
    return lista[int(eleccion_correcta) - 1]


def mostrar_archivos(ruta, formato):
    ruta_ = Path(ruta)
    lista_archivos = []
    contador = 1
    for file in ruta_.glob(formato):
        _str = str(file.name)
        print(f'[{contador}] - {_str}')
        lista_archivos.append(file)
        contador += 1
    return lista_archivos


def crear_carpeta(ruta):
    existe = False
    while not existe:
        try:
            print('Escribe el nombre de la nueva carpeta: ')
            nombre_carpeta = input()
            ruta_nueva = Path(ruta, nombre_carpeta)
            if not os.path.exists(ruta_nueva):
                Path.mkdir(ruta_nueva)
                print(f'La carpeta {nombre_carpeta} ha sido creada')
                existe = True
            else:
                print('Lo siento, esa carpeta ya existe')
        except KeyboardInterrupt:
            break


def leer_archivo_text(file):
    print(Path.read_text(file))


def eliminar_archivo(file):
    Path(file).unlink()
    print(f'La receta {file.name} ha sido eliminada')


def eliminar_carpeta(ruta):
    send2trash.send2trash(Path(ruta))
    print(f'La carpeta {Path(ruta).name} ha sido eliminada')


def all_search_file(ruta, ext):
    lst = []
    paths = Path(ruta).glob('**/*' + ext)
    for path in paths:
        lst.append(path)
    return lst


def move_files(origin, destination, ext):
    ext = '*' + ext
    allfiles = glob.glob(os.path.join(origin, ext), recursive=True)
    for file_path in allfiles:
        dst_path = os.path.join(destination, os.path.basename(file_path))
        shutil.move(file_path, dst_path)
    return True


def create_folder(route, name):
    if not os.path.exists(route):
        os.mkdir(Path(route, name))
    else:
        pass