#Autor: Popławski Damian
from tkinter import filedialog
from tkinter import *
from zipfile import ZipFile
from tkinter import messagebox
import os

window = Tk()
window.title("program do dekompresji")
window.geometry("650x400")


def extract():
    folder = filedialog.askopenfilename()
    with ZipFile(folder, 'r') as zip:
        messagebox.showinfo(title="Wypakowywanie", message="trwa wypakowywanie", )
        zip.extractall()
        messagebox.showinfo(title="Gotowe", message="jest Git!")


def close():
    window.quit()


extract_button = Button(window, text="wypakuj", width=100, bg='light green', command=extract)
extract_button.grid(row=0, column=3, sticky=N + S + E + W)

close_button = Button(window, text="wyjście", width=100, bg='red', command=close)
close_button.grid(row=1, column=3, sticky=N + S + E + W)

totalRows = 3
totalCols = 3

for row in range(totalRows + 1):
    window.grid_rowconfigure(row, weight=1)

for col in range(totalCols + 1):
    window.grid_columnconfigure(col, weight=1)

window.mainloop()
