"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""


def parsing_path(path: str) -> tuple:
    name = path.split('\\')[-1]
    extension = name.split('.')[-1]
    return (path, name, extension)


example = r'E:\GB course\Analyst\Python\names.txt'
if __name__ == '__main__':
    print(parsing_path(example))
