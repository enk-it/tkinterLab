import tkinter as tk
from tkinter import ttk
from utils.validate import validate_float


class Entry:
    def __init__(self, frame, text, row, callback, strict_positive=False, max_len=-1):
        self.max_len = max_len
        self.strict_positive = strict_positive
        self.callback = callback

        self.variable = tk.StringVar()
        self.variable.trace('w', self.onChange)

        self.error_variable = tk.StringVar()

        self.label = tk.Label(frame, text=text)
        self.label.grid(row=row, column=1)
        self.entry = tk.Entry(frame, textvariable=self.variable)
        self.entry.grid(row=row, column=2)

        self.error_label = tk.Label(frame, text='', textvariable=self.error_variable)
        self.error_label.grid(row=row, column=3)

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
        elif self.max_len != -1 and len(value) > self.max_len:
            self.valid = False
            self.error = f'Значение не может быть больше {self.max_len} знаков'
            self.error_variable.set(self.error)
            self.entry.configure(background='red')
        else:
            self.valid = True
            self.error = ''
            self.entry.configure(background='white')
            self.error_variable.set(self.error)
