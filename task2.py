#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def show_all_subdir(path, space_factor=0):
    file_list = os.listdir(path)
    for file in file_list:
        space = ' ' * space_factor
        print(space + file)
        try:
            show_all_subdir(path + f'/{file}', space_factor=space_factor + 1)
        except:
            continue


def main():
    current_path = 'C:/Users'
    while True:
        comand = input(current_path + '>').split()
        match comand[0]:
            case 'cd':
                current_path = comand[1]
            case 'list':
                show_all_subdir(current_path)


if __name__ == '__main__':
    main()