import json
import os
import sys


def load_json_data(filepath):
    if not os.path.exists(filepath):
        print ('Не верный путь до файла\файла не существует,перезапустите программу и введите правильные данные')
        sys.exit()
        return None
    with open(filepath, 'r', encoding = 'utf-8') as file_handler:
        return json.load(file_handler)

def pretty_print_json(data):
    print(json.dumps(data, indent = 4,encure_ascii=False))                

if __name__ == '__main__':
    pass

print('Введите путь до файла(если файл лежит'
      'в этойже директории,то введите просто имя файла)')
path = str(input())
file_json = load_json_data(path)
pretty_print_json(file_json)
