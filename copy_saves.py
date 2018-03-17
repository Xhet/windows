import pathlib
import logging
import shutil
import datetime
import time
import os
import errno


def main(src, dest):
    pathBk = list(pathlib.Path(dest).glob("*"))
    pathSrc = list(pathlib.Path(src).glob("*"))
    st = datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d+%H_%M')
    for file in pathSrc:
        fname = os.path.basename(file)
        print(str(file) + " este es el archivo a copiar \n")
        destino = (f"{dest}/{fname}.{st}")
        print(destino + " Este es el nombre que tendra en el destino \n")

        try:
#            shutil.copytree(str(file), f"{destino}")
            print("helo")

        except Exception as e:
            if e.errno == errno.ENOTDIR:
                print('not')
#                shutil.copy(str(file), f"{destino}")
            else:
                logs(file, e)
                exit(1)
    if len(pathBk) >= 5:
        print(str(len(pathBk)) + " string")
        clean(pathBk)


def clean(abs):
    sort = sorted(abs, key=lambda l: os.stat(l).st_ctime)
    for file in sort[:15]:
        print(file)
        try:
#            shutil.rmtree(file)
            print(str(file) + " is a Dir")
        except Exception as e:
            if e.errno == errno.ENOTDIR:
#                os.remove(file)
                print(str(file) + ' Removed')
            else:
                logs(file, e)
                exit(1)


def logs(arch, ex):
    logger = logging.getLogger("CopyFiles")
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(filename="CopyErrors.log",
                                  encoding="utf-8",
                                  mode="w")
    handler.setFormatter(logging.Formatter(
        "%(asctime)s - [%(levelname)s] %(name)s: %(message)s"))
    logger.addHandler(handler)
    logger.warning(f"{arch} could not be copied.\n"
                   f"{type(ex).__name__}: {ex}")


if __name__ == '__main__':
    main("/home/likewise-open/NT/ecasado/Pictures",
         "/home/likewise-open/NT/ecasado/Downloads/docs/do_delete")
