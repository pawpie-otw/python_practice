import os
import requests as req


def gen_get_files(start_dir):
    for file in os.listdir(start_dir):
        if file.endswith('radek.txt'):
            print(os.path.join(start_dir, file))
            yield os.path.join(start_dir, file)


def gen_get_file_lines(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.rstrip()


def check_webpage(url):
    try:
        response = req.get(url)
        if response.status_code == 200:
            return True
    except Exception:
        return False


path = r'C:\Users\profsor500\Desktop\python\nauka_samodzielna\zadania treningowe'
spliter = r'\\'
for file in gen_get_files(r'C:\Users\profsor500\Desktop\python\nauka_samodzielna\zadania treningowe\files'):
    for line in gen_get_file_lines(file):
        print(f"{file} - {line} - {check_webpage(line)}")
