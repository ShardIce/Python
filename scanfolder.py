#import glob
import shutil
import os
import pathlib
from pathlib import Path

FILES_INPUT = 'C:\\Users\\admin\\Desktop\\python\\rookie' # Входные файлы
FILES_OUTPUT = 'C:\\Users\\admin\\Desktop\\python\\' # Выходные файлы

for dirpath, dirnames, filenames in os.walk(FILES_INPUT):
    for filename in filenames:
        if os.listdir(FILES_INPUT):
            if not os.path.isdir(filename):
                for filename in filenames:
                    os.mkdir(os.path.splitext(filename)[0])
                    print(Path(FILES_OUTPUT, os.path.splitext(filename)[0]))
                    move_files = Path(FILES_OUTPUT, os.path.splitext(filename)[0])
                    shutil.move(move_files)
        else:
                    print("НЕТ НИЧЕГО")
