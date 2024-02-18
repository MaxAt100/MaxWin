import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import requests
import zipfile
import shutil
import win32com.client

def download_and_extract(url, extract_to):
    response = requests.get(url)
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(response.content)
        tmp_file_path = tmp_file.name
    with zipfile.ZipFile(tmp_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(tmp_file_path)

def create_shortcut(source, shortcut_name, icon_path):
    shell = win32com.client.Dispatch("WScript.Shell")
    desktop = shell.SpecialFolders("Desktop")
    shortcut = shell.CreateShortCut(os.path.join(desktop, f"{shortcut_name}.lnk"))
    shortcut.Targetpath = source
    shortcut.IconLocation = icon_path
    shortcut.save()

def main():
    root = tk.Tk()
    root.withdraw()  # Скрыть основное окно tkinter

    response = messagebox.askyesno("Установка модулей", "Необходимо установить модули! Нажмите Да, если вы хотите это сделать, или Нет")
    if response:
        subprocess.run(["Module.exe"], check=True)
    else:
        return

    response = messagebox.askyesno("Проверка соединения", "Для продолжения, убедитесь что у вас отличное соединение к интернету. Если всё хорошо, нажмите \"Да\", если что-то не так, нажмите \"Нет\"")
    if response:
        os.makedirs("C:\\Program Files\\MaxWin", exist_ok=True)
        download_and_extract("https://github.com/MaxAt100/MaxWin/archive/refs/heads/main.zip", "C:\\Program Files\\MaxWin")
        create_shortcut("C:\\Program Files\\MaxWin\\Zapusk.bat", "MaxWin", "C:\\Program Files\\MaxWin\\exe\\MaxWin.ico")
        subprocess.run(["C:\\Program Files\\MaxWin\\Zapusk.bat"], check=True)
    else:
        return

if __name__ == "__main__":
    main()