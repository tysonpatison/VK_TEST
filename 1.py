import os
import requests
import subprocess


url = 'https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=0&' \
      'confirm=t'

file_name = 'settings.reg'

def find_game_directory(path, target_directory):
    for root, dirs, files in os.walk(path):
        if target_directory in dirs:  # Ищем нужную директорию
            game_directory = os.path.join(root, target_directory)
            return game_directory

    raise FileNotFoundError

def exec_file(href: str):
    subprocess.Popen(href)

def download_file(url:str, file_name: str):
    resp = requests.get(url)
    with open(file_name, "wb") as file:
        file.write(resp.content)

    if resp.status_code != 200:
        raise requests.exceptions.HTTPError

def add_to_register(file_name: str):
    subprocess.Popen("reg import {}".format(file_name))

def main():
    directory = find_game_directory(os.getenv('SystemDrive') + '/', 'Goose Goose Duck')
    os.chdir(directory)
    download_file(url, file_name)
    add_to_register(file_name)
    exec_file('Goose Goose Duck.exe')


if __name__ == '__main__':
    main()





