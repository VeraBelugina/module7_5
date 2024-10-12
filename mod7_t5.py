import os
import time

directory = r'C:\Urban\Tasks'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

print(f' Обнаружен файл: {file}\n Путь: {filepath}\n Размер: {file_size} байт\n Время изменения: {formatted_time}\n '
      f'Родительская директория: {parent_dir}')
