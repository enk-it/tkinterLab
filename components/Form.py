import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.validate import validate_float
from .Entry import Entry
from .CheckBox import CheckBox
from .ComboBox import ComboBox


class Form:
    def __init__(self, submit_callback):
        self.submit_callback = submit_callback
        window = tk.Tk()

        window.title("Табулирование функции tkinter")
        window.geometry("800x600")

        label = tk.Label(window, text = "Функция y = f(x)")
        label.pack()

        frame = tk.Frame(window, padx=10, pady=10)
        frame.pack(expand=True)

        self.start = Entry(frame, 'Введите начальное значение', 3)
        self.end = Entry(frame, 'Введите конечное значение', 4)
        self.step = Entry(frame, 'Введите значение шага', 5, strict_positive=True)
        self.show = CheckBox(frame, 'Показать график', 6)
        self.options = ComboBox(frame, 'Действия с графиком', 7, ["Показать", "Сохранить в файл", "Показать и сохранить", "Игнорировать"])

        
        submit = tk.Button(frame, text='Табулировать', command=self.on_submit_click)
        submit.grid(row=8, column=2)
        window.mainloop()

    def get_values(self):
        return {
        'start': float(self.start.variable.get()),
        'end': float(self.end.variable.get()),
        'step': float(self.step.variable.get()),
        'graph': self.show.variable.get(),
        'options': self.options.variable.get()
        }



    def is_fields_valid(self):
        for field in [self.start, self.end, self.step]:
            if not field.valid:
                return False

        if float(self.start.variable.get()) > float(self.end.variable.get()):
            return False

        return True


    def on_submit_click(self):
        if self.is_fields_valid():
            current_values = self.get_values()
            self.submit_callback(current_values)
        else:
            messagebox.showerror(title='Ошибка!', message='Введены недопустимые значения!')



