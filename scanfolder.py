import shutil
import os

FILES_INPUT = 'C:\\Users\\admin\\Desktop\\python\\rookie' # Входные файлы
FILES_OUTPUT = 'C:\\Users\\admin\\Desktop\\python\\' # Выходные файлы

for dirpath, dirnames, filenames in os.walk(FILES_INPUT):
    for filename in filenames:
        if os.listdir(FILES_INPUT):
            if not os.path.isdir(filename):
                for filename in filenames:
                    os.mkdir(os.path.splitext(filename)[0])
                    shutil.move(os.path.join(FILES_INPUT, filename), FILES_OUTPUT)
        else:
                    print("НЕТ НИЧЕГО")
