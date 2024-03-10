import tkinter as tk
from tkinter import ttk
from utils.validate import validate_float


class Entry:
    def __init__(self, frame, text, row, callback, strict_positive=False):
        self.strict_positive = strict_positive
        self.callback = callback

        self.variable = tk.StringVar()
        self.variable.trace('w', self.onChange)

        self.label = tk.Label(frame, text=text)
        self.label.grid(row=row, column=1)
        self.entry = tk.Entry(frame, textvariable=self.variable)
        self.entry.grid(row=row, column=2)

        self.valid = False

        self.error = 'Поле не может быть пустым'

    def onChange(self, *args):
        value = self.variable.get()
        self.validate(value)
        self.callback()

    def validate(self, value):
        if value == '':
            self.valid = False
            self.error = 'Поле не может быть пустым'
            self.entry.configure(background='white')
        elif not validate_float(value):
            self.valid = False
            self.error = f'Неверное значение: {self.variable.get()}'
            self.entry.configure(background='red')
        elif self.strict_positive and float(value) <= 0:
            self.valid = False
            self.error = 'Значение не может быть отрицательным'
            self.entry.configure(background='red')
        else:
            self.valid = True
            self.error = ''
            self.entry.configure(background='white')
