# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def path_triple(path_str):
    # разбираем заданную строку на части по "\"
    *path, file_full = path_str.split('\\')
    # собираем путь до файла
    path = '\\'.join(path) + '\\'
    # разбираем на имя + расширение по '.'
    file_name, file_extension = file_full.split('.')

    return (path, file_name, file_extension)


path_str = 'D:\GB\Python_hard\Task11\Task11.py'
print(path_triple(path_str))