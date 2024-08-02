import time
from colorama import init, Fore, Style, Back
import webbrowser
import os
import subprocess
import platform

def get_os_info():
    os_info = platform.system()
    return os_info

def get_os_version():
    os_version = platform.version()
    return os_version

print(Fore.LIGHTMAGENTA_EX + 'qConsole',Style.RESET_ALL)
print(os.getlogin(), '|', get_os_info(), get_os_version())
print(Style.RESET_ALL)
print('Type ? to help')

current_directory = os.getcwd()

def say(text):
    print(Fore.LIGHTMAGENTA_EX + text)
    print(Style.RESET_ALL)

def open_url(url):
    print(Fore.LIGHTMAGENTA_EX + 'Opening ' + url)
    print(Style.RESET_ALL)
    time.sleep(0.5)
    webbrowser.open(url)

def open_file(file):
    try:
        subprocess.Popen(file, shell=True)
        print(Fore.LIGHTMAGENTA_EX + 'Opening ' + file)
        print(Style.RESET_ALL)
    except:
        print(Fore.RED + 'Error: Could not open ' + file)
        print(Style.RESET_ALL)

def list_directory(path):
    files = os.listdir(path)
    for file in files:
        print(Fore.LIGHTMAGENTA_EX + file)
    print(Style.RESET_ALL)

def internet_search(query):
    search_url = "https://www.google.com/search?q=" + query
    print(Fore.LIGHTMAGENTA_EX + 'Searching for ' + query + '...')
    print(Style.RESET_ALL)
    time.sleep(0.5)
    webbrowser.open(search_url)

def open_file(file):
    try:
        subprocess.Popen(file, shell=True)
        print(Fore.LIGHTMAGENTA_EX + 'Opening ' + file)
        print(Style.RESET_ALL)
    except:
        print(Fore.RED + 'Error: Could not open ' + file)
        print(Style.RESET_ALL)

def change_directory(path):
    global current_directory

    if path == 'reset':
        current_directory = os.getcwd()
        print(Fore.LIGHTMAGENTA_EX + 'Reset directory')
        print(Style.RESET_ALL)
    else:
        try:
            os.chdir(path)
            current_directory = os.getcwd()
            print(Fore.LIGHTMAGENTA_EX + 'Changed directory to ' + path)
            print(Style.RESET_ALL)
        except:
            print(Fore.RED + 'Error: Could not change directory to ' + path)
            print(Style.RESET_ALL)

while True:
    v = input()

    if v == '?':
        print(Fore.MAGENTA + 'Commands:')
        print(Style.RESET_ALL)
        print('say "Your text" - Say text')
        print('uo "URL" - Open URL')
        print('listdir "Path" - List files in directory')
        print('isearch "Query" - Search the internet')
        print('open "File" - Open a file or program')
        print('cd "Path" - Change directory')
        print('ls - Lock screen')

    elif v.startswith('say '):
        text = v[4:]
        say(text)
    elif v.startswith('uo '):
        url = v[3:]
        open_url(url)
    elif v.startswith('listdir '):
        path = v[8:]
        list_directory(os.path.join(current_directory, path))
    elif v.startswith('isearch '):
        query = v[8:]
        internet_search(query)
    elif v.startswith('open '):
        file = v[5:]
        open_file(os.path.join(current_directory, file)) 
    elif v.startswith('cd '):
        path = v[3:]
        change_directory(os.path.join(current_directory, path)) 

    elif v == 'ls':
        print("\033[H\033[J")
        print(Fore.RED + 'Computer is blocked. Press enter')
        print(Fore.RED + 'Компьютер заблокирован. Нажмите enter')
        input()
        os.system('rundll32.exe user32.dll,LockWorkStation')
