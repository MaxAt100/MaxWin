import tkinter as tk
from tkinter import messagebox
import os

# Функция, которая будет вызываться при нажатии кнопки "Да"
def on_yes():
    os.system('start start.exe')
    os.system('start sound.exe')

# Функция, которая будет вызываться при нажатии кнопки "Нет"
def on_no():
    os.system('start Modules.exe')

# Создание главного окна
root = tk.Tk()
root.withdraw()  # Скрыть основное окно

# Показать диалоговое окно с вопросом
response = messagebox.askquestion("Установка модулей", "Перед началом, вам необходимо установить модули. Нажмите 'Нет', чтобы установка началась сама, или 'Да' для продолжения.")

# Обработка ответа
if response == 'yes':
    on_yes()
else:
    on_no()
