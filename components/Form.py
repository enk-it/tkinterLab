import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from tkinter import Entry
from tkinter import Frame
from tkinter import Label


class Form:
    def __init__(self):
        window = tk.Tk()
        window.title("Табулирование функции tkinter")

        frame = Frame(window, padx=10, pady=10)
        frame.pack(expand=True)

        start_label = Label(frame, text="Введите начальное значение")
        start_label.grid(row=3, column=1)

        start_entry = Entry(frame, )
        start_entry.grid(row=3, column=2)

        end_label = Label(frame, text="Введите конечное значение")
        end_label.grid(row=4, column=1)

        end_entry = Entry(frame, )
        end_entry.grid(row=4, column=2)

        submit = Button(frame, text='Табулировать', )
        submit.grid(row=5, column=2)

        window.mainloop()


Form()