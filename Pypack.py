from pathlib import Path
import send2trash
import datetime
import zipfile
import shutil
import time
import math
import os


def unpack(**kwargs):
    inicio = time.time()
    today = datetime.date.today()
    name = f'Uncompress_Folder_{today.day}_{today.month}_{today.year}'
    home = os.getcwd()
    f = Path(home, name)
    try:
        if 'folder' in kwargs and 'origin' in kwargs and 'destination' in kwargs:
            shutil.copy(Path(kwargs.get('origin'),kwargs.get('folder')), str(Path(kwargs.get('destination'))))
            os.chdir(str(Path(kwargs.get('destination'))))
            home = os.getcwd()
            shutil.unpack_archive(kwargs.get('folder'), f,
                                  str(Path(kwargs.get('folder')).suffix).replace('.', ''))
            file = Path(home, kwargs.get('folder'))
            send2trash.send2trash(file)
        elif 'folder' in kwargs and 'origin' in kwargs:
            os.chdir(str(Path(kwargs.get('origin'))))
            home = os.getcwd()
            f = Path(home, name)
            shutil.unpack_archive(kwargs.get('folder'), f,
                                  str(Path(kwargs.get('folder')).suffix).replace('.', ''))
        elif 'folder' in kwargs and 'destination' in kwargs:
            shutil.copy(kwargs.get('folder'), str(Path(kwargs.get('destination'))))
            os.chdir(str(Path(kwargs.get('destination'))))
            home = os.getcwd()
            f = Path(home, name)
            shutil.unpack_archive(kwargs.get('folder'), f,
                                  str(Path(kwargs.get('folder')).suffix).replace('.', ''))
            file = Path(home, kwargs.get('folder'))
            send2trash.send2trash(file)
        elif 'folder' in kwargs:
            shutil.unpack_archive(kwargs.get('folder'), f,
                                  str(Path(kwargs.get('folder')).suffix).replace('.', ''))
        else:
            return '\n...Debes de ingresar almenos una constante correcta'
    except ValueError:
        return f"\n...La carpeta comprimida '{kwargs.get('folder')}' no se puede descompimir."
    except shutil.ReadError:
        return f"\n...La carpeta comprimida '{kwargs.get('folder')}' no existe,\ntalvez se encuentre en otra direccion..."
    except FileNotFoundError:
        return f"\n...Revisa bien los datos ingresados"
    else:
        fin = time.time()
        duracion = fin - inicio
        return f'\nUnpack in the folder "{name}"\nTime spend: {math.ceil(duracion)} seconds'


def pack(**kwargs):
    inicio = time.time()
    today = datetime.date.today()
    name = f'Compress_Folder_{today.day}_{today.month}_{today.year}.zip'
    try:
        if 'files' in kwargs and 'origin' in kwargs and 'destination' in kwargs:
            Zip = zipfile.ZipFile(Path(kwargs.get('destination'), name), 'w')
            if type(kwargs.get('files')) == list or type(kwargs.get('files')) == tuple:
                for i in range(len(kwargs.get('files'))):
                    Zip.write(Path(kwargs.get('origin'), f"{kwargs.get('files')[i]}"))
            else:
                if kwargs.get('files') == 'all':
                    for carpetas, subcarpetas, archivos in os.walk(kwargs.get('origin'), topdown=True):
                        for a in archivos:
                            Zip.write(os.path.join(carpetas,a))
                else:
                    Zip.write(Path(kwargs.get('origin'),f"{kwargs.get('files')}"))
            Zip.close()
        elif 'files' in kwargs and 'origin' in kwargs:
            Zip = zipfile.ZipFile(name, 'w')
            if type(kwargs.get('files')) == list or type(kwargs.get('files')) == tuple:
                for i in range(len(kwargs.get('files'))):
                    Zip.write(Path(kwargs.get('origin'),f"{kwargs.get('files')[i]}"))
            else:
                if kwargs.get('files') == 'all':
                    for carpetas, subcarpetas, archivos in os.walk(kwargs.get('origin'), topdown=True):
                        for a in archivos:
                            Zip.write(os.path.join(carpetas, a))
                else:
                    Zip.write(Path(kwargs.get('origin'),f"{kwargs.get('files')}"))
            Zip.close()
        elif 'files' in kwargs and 'destination' in kwargs:
            Zip = zipfile.ZipFile(Path(kwargs.get('destination'), name), 'w')
            if type(kwargs.get('files')) == list or type(kwargs.get('files')) == tuple:
                for i in range(len(kwargs.get('files'))):
                    Zip.write(kwargs.get('files')[i])
            else:
                if kwargs.get('files') == 'all':
                    for carpetas, subcarpetas, archivos in os.walk(os.getcwd()):
                        for a in archivos:
                            Zip.write(a)
                else:
                    Zip.write(kwargs.get('files'))
            Zip.close()
        elif 'files' in kwargs:
            Zip = zipfile.ZipFile(name, 'w')
            if type(kwargs.get('files')) == list or type(kwargs.get('files')) == tuple:
                for i in range(len(kwargs.get('files'))):
                    Zip.write(kwargs.get('files')[i])
            else:
                if kwargs.get('files') == 'all':
                    for carpetas, subcarpetas, archivos in os.walk(os.getcwd(), topdown=True):
                        for a in archivos:
                            Zip.write(os.path.join(carpetas, a))
                else:
                    Zip.write(kwargs.get('files'))
            Zip.close()
        else:
            return '\n...Debes de ingresar almenos una constante correcta'
    except FileNotFoundError:
        return f"\n...Revisa bien el nombre de los datos ingresados"
    else:
        fin = time.time()
        duracion = fin - inicio
        return f'\npack in the folder "{name}"\nTime spend: {math.ceil(duracion)} seconds'
