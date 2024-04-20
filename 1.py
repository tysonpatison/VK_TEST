import os
import requests
import subprocess

url = 'https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=0&' \
      'confirm=t'

file_name = 'settings.reg'
game_name = 'Goose Goose Duck'


def find_game_directory(path, target_directory):
    for root, dirs, files in os.walk(path):
        if target_directory in dirs:
            game_directory = os.path.join(root, target_directory)
            return game_directory

    raise FileNotFoundError


def execute_game(href: str):
    subprocess.Popen(href)


def download_file(href: str, name: str):
    resp = requests.get(href)
    with open(name, "wb") as file:
        file.write(resp.content)

    if resp.status_code != 200:
        raise requests.exceptions.HTTPError


def add_to_register(name: str):
    subprocess.Popen("reg import {}".format(name))


def main():
    directory = find_game_directory(os.getenv('SystemDrive') + '/', game_name)
    os.chdir(directory)
    download_file(url, file_name)
    add_to_register(file_name)
    execute_game("{}.exe".format(game_name))


if __name__ == '__main__':
    main()
