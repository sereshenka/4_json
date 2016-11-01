#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
import os
import sys
import argparse


def load_json_data(file_path):
    if not os.path.exists(file_path):
        return None
    else:
        with open(file_path, 'r', encoding = 'utf-8') as file_handler:
                return json.load(file_handler)  
    
    
def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()
        

def read_arguments():
    """
    использую с join,чтобы программа работала при указании пути,в котором папка
    может содержать в названии пробел(C:\\Users\\New User\\file.format)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', help='Укажите путь к файлу в формате .json', nargs = '+')
    arguments = parser.parse_args().json
    try :
        file_path = ' '.join(arguments)
    except TypeError:
        return None, parser
    return file_path, parser  


def pretty_print_json(data):
    try:
        print(json.dumps(data, indent = 4,ensure_ascii = False))
    except UnicodeEncodeError:
        print('Ошибка с кодировками в выводе в консоль')
        

if __name__ == '__main__':
    while True:
        load_win_unicode_console()
        file_path,parser = read_arguments()
        if file_path is None:
            parser.print_help()
            break
        try:
            json_file = load_json_data(file_path)
        except ValueError:
            print('Это не json')
            break
        if json_file is None:
            print('Не верный путь до файла\файла не существует,перезапустите программу и введите правильные данные')
            break
        pretty_print_json(json_file)
        break
