# fylhtq7779 - program
# Beamer XD - materials file from Skin Helper

from tkinter import ttk
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
# from wand import image

import shutil
import os

path = ''
current_car = ''
current_car_name = ''
name = ''
filename = ''
directory = ''


def make_skin():
    global path
    global name
    global current_car_name
    name = name_skin.get()
    game_name = game_name_skin.get()
    current_car_name = car_choice.get()
    init_car()
    path = 'temp/vehicles/' + current_car + '/' + name
    jbeam_path = path + '/' + current_car + '.jbeam'
    json_path = path + '/materials.json'
    os.makedirs(path)
    print(jbeam_path)
    if name:
        with open('template/template.jbeam', 'r') as file:
            repl = file.read().replace('RAD', 'This skin make by computer, the future is near')
            repl = file.read().replace('AUT', 'Program by fylhtq7779')
            repl = file.read().replace('NAME', name)
            repl = repl.replace('GNAM', game_name)
            repl = repl.replace('CARSS', current_car)
        with open(jbeam_path, 'w') as file:
            file.writelines(repl)
    if game_name:
        with open('template/' + current_car + '.json', 'r') as file:
            repl = file.read().replace('SKINNAME', name)
        with open(json_path, 'w') as file:
            file.writelines(repl)
        create_zip()


def create_zip():
    if filename[-3:] == 'dds':
        choose_directory()
        name_dds = current_car + '_skin_' + name + '.dds'
        shutil.copy2(filename, path + '/' + name_dds)
        shutil.make_archive(name, 'zip', 'temp')
        shutil.rmtree('temp')
        mb.showinfo(title='Успешно', message='Скин создан')
        shutil.copy2(name + '.zip', directory)
    # elif filename[-3:] == 'png':
    #     with image.Image(filename=filename) as img:
    #         img.compression = 'dxt5'
    #         name_dds = current_car + '_skin_' + name + '.dds'
    #         img.save(filename=path + '/' + name_dds)
    #         shutil.make_archive(name, 'zip', 'temp')
    #         shutil.rmtree('temp')
    #         mb.showinfo(title='Успешно', message='Скин создан')


def choose_file():
    global filename
    filetypes = (("Изображение", "*.dds"),)
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                  filetypes=filetypes)


def choose_directory():
    global directory
    directory = fd.askdirectory(title="Открыть папку", initialdir="/")


def init_car():
    global current_car
    if current_car_name == 'Autobello Piccolina':
        current_car = 'autobello'
        print(current_car)

    if current_car_name == 'Ibishu 200BX':
        current_car = 'coupe'
        print(current_car)

    if current_car_name == 'Civetta Bolide':
        current_car = 'bolide'
        print(current_car)

    if current_car_name == 'Burnside Special':
        current_car = 'burnside'
        print(current_car)

    if current_car_name == 'Cherrier Vivace/Tograc':
        current_car = 'vivace'
        print(current_car)

    if current_car_name == 'ETK 800 Series':
        current_car = 'etk800'
        print(current_car)

    if current_car_name == 'ETK K-Series':
        current_car = 'etkc'
        print(current_car)

    if current_car_name == 'ETK I-Series':
        current_car = 'etki'
        print(current_car)

    if current_car_name == 'Ibishu Covet':
        current_car = 'hatch'
        print(current_car)

    if current_car_name == 'Ibishu Hopper':
        current_car = 'hopper'
        print(current_car)

    if current_car_name == 'Ibishu Pessima':
        current_car = 'pessima'
        print(current_car)

    if current_car_name == 'Ibishu Miramar':
        current_car = 'miramar'
        print(current_car)

    if current_car_name == 'Ibishu Pigeon':
        current_car = 'pigeon'
        print(current_car)

    if current_car_name == 'Ibishu Wigeon':
        current_car = 'wigeon'
        print(current_car)

    if current_car_name == 'Bruckell LeGran':
        current_car = 'legran'
        print(current_car)

    if current_car_name == 'Bruckell Moonhawk':
        current_car = 'moonhawk'
        print(current_car)

    if current_car_name == 'Hirochi SBR4':
        current_car = 'sbr'
        print(current_car)

    if current_car_name == 'Bruckell Moonhawk':
        current_car = 'moonhawk'
        print(current_car)

    if current_car_name == 'Hirochi Sunburst':
        current_car = 'sunburst'
        print(current_car)

    if current_car_name == 'Gavril H-Series':
        current_car = 'van'
        print(current_car)

    if current_car_name == 'Gavril Bluebuck':
        current_car = 'bluebuck'
        print(current_car)

    if current_car_name == 'Gavril Grand Marshal':
        current_car = 'fullsize'
        print(current_car)

    if current_car_name == 'Gavril Bluebuck':
        current_car = 'bluebuck'
        print(current_car)

    if current_car_name == 'Gavril T-Series':
        current_car = 'semi'
        print(current_car)

    if current_car_name == 'Gavril D-Series':
        current_car = 'pickup'
        print(current_car)

    if current_car_name == 'Gavril Roamer':
        current_car = 'roamer'
        print(current_car)

    if current_car_name == 'Gavril Barstow':
        current_car = 'barstow'
        print(current_car)

    if current_car_name == 'Soliad Wendover':
        current_car = 'wendover'
        print(current_car)

    if current_car_name == 'Gavril Barstow':
        current_car = 'barstow'
        print(current_car)

    if current_car_name == 'Wentward DT40L':
        current_car = 'citybus'
        print(current_car)


cars = (
    'Autobello Piccolina', 'Burnside Special', 'Cherrier Vivace/Tograc', 'Civetta Bolide', 'ETK 800 Series',
    'ETK K-Series',
    'ETK I-Series', 'Ibishu 200BX', 'Ibishu Covet', 'Ibishu Hopper', 'Ibishu Pessima', 'Ibishu Miramar',
    'Ibishu Pessima',
    'Ibishu Pigeon', 'Ibushu Wigeon', 'Bruckell LeGran', 'Bruckell Moonhawk', 'Hirochi SBR4', 'Hirochi Sunburst',
    'Gavril H-Series', 'Gavril Bluebuck', 'Gavril Grand Marshal', 'Gavril T-Series', 'Gavril D-Series', 'Gavril Roamer',
    'Gavril Barstow', 'Soliad Wendover', 'Wentward DT40L')

root = tk.Tk()

root.geometry(f"300x400+1300+700")
root.title('Skin Creator v1 by fylhtq7779')
root.resizable(False, False)

car_choice = ttk.Combobox(root, values=cars)
car_choice.current(0)
name_skin = ttk.Entry(root)
game_name_skin = ttk.Entry(root)


def frame():
    ttk.Label(text='Выбор машины').pack()
    car_choice.pack()
    ttk.Label(text='Имя скина(одно слово)').pack()
    name_skin.pack()
    ttk.Label(text='Название в игре').pack()
    game_name_skin.pack()
    ttk.Button(root, text='Выбрать скин', command=choose_file).pack()
    ttk.Button(root, text='Создать мод', command=make_skin).pack()


frame()
root.mainloop()
