#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import sys
import argparse


def load_json_data(file_path):
    if not os.path.exists(file_path):
        print ('Не верный путь до файла\файла не существует,перезапустите программу и введите правильные данные')
        return None
    with open(file_path, 'r', encoding = 'utf-8') as file_handler:
        return json.load(file_handler)

def create_parser():
     parser = argparse.ArgumentParser()
     parser.add_argument('--json', help='Укажите путь к фаилу в формате .json')
     file_json = parser.parse_args().json
     if not file_json:
         parser.print_help()
         return None
     else:
         return (file_json)
    

def pretty_print_json(data):
    print(json.dumps(data, indent = 4,ensure_ascii=False))                

if __name__ == '__main__':
    file_path = create_parser()
    open_json = load_json_data(file_path)
    pretty_print_json(open_json)
