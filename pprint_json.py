#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
import os
import sys
import argparse


def load_json_data(file_path):
    if not os.path.exists(file_path):
        print ('Не верный путь до файла\файла не существует,перезапустите программу и введите правильные данные')
        return None
    else:
        return (open_json(file_path))
    
        
def open_json(file_path):
    try:
        with open(file_path, 'r', encoding = 'utf-8') as file_handler:
            return json.load(file_handler)
    except ValueError :
        print('Это не json файл')
        return None
    
    
def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()
        

def read_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', help='Укажите путь к файлу в формате .json', nargs = '?')
    file_json = parser.parse_args().json
    return (existence_of_input(file_json,parser))


def existence_of_input(file_json,parser):
    if not file_json:
        parser.print_help()
        return None
    else:
        return (file_json)
        


def pretty_print_json(data):
    try:
        print(json.dumps(data, indent = 4,ensure_ascii = False))
    except UnicodeEncodeError:
        print('Ошибка с кодировками в выводе в консоль')
        

if __name__ == '__main__':
    load_win_unicode_console()
    file_path = read_arguments()
    if file_path is not None:
        json_file = load_json_data(file_path)
        if json_file is not None:
            pretty_print_json(json_file)
