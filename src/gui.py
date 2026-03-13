import sys
import os
import customtkinter as ctk
import threading
from center import center

print('Доброго времени суток')

base_path = ''

try:
    base_path = sys._MEIPASS
except Exception:
    base_path = os.path.abspath(".")

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

app = ctk.CTk()
app.title('DES WB')
app.geometry('230x150')
app.iconbitmap(os.path.join(base_path, "app_icon.ico"))
app.resizable(False, False)

def input_params():

    local_query = query.get()
    local_choice_city = choice_city.get()
    
    if not local_query or not local_choice_city or local_choice_city == 'Выберите город':
        print('Заполните все данные')
        return

    thread = threading.Thread(target = center, args = (local_query, local_choice_city, base_path))
    thread.start()

query = ctk.CTkEntry(app, placeholder_text = 'Поисковый запрос')
query.grid(row = 0, column = 0, padx = 45, pady = 10)

city = ['Москва', 'Санкт-Петербург', 'Казань', 'Самара', 'Екатеринбург', 'Владивосток']

choice_city = ctk.CTkOptionMenu(app, values = city)
choice_city.set('Выберите город')
choice_city.grid(row = 1, column = 0, padx = 10, pady = 10)

button_input_params = ctk.CTkButton(app, text = 'Запуск', command = input_params)
button_input_params.grid(row = 2, column = 0, padx = 10, pady = 0)


app.mainloop()