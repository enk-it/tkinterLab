import tkinter as tk
from tkinter import messagebox
from components.Entry import Entry
from components.CheckBox import CheckBox
from components.ComboBox import ComboBox
from components.Text import Text


class Form:
    def __init__(self, submit_callback):
        self.submit_callback = submit_callback
        window = tk.Tk()
        self.text_error = ''

        window.attributes('-type', 'utility ')

        window.title("Табулирование функций tkinter")
        window.geometry("800x600")

        label = tk.Label(window, text="Функция y = f(x)")
        label.pack()

        frame = tk.Frame(window, padx=10, pady=10)
        frame.pack(expand=True)

        self.start = Entry(frame, 'Введите начальное значение', 3, self.update_error_field)
        self.end = Entry(frame, 'Введите конечное значение', 4, self.update_error_field)
        self.step = Entry(frame, 'Введите значение шага', 5, self.update_error_field, strict_positive=True)
        self.show_table = CheckBox(frame, 'Показать таблицу', 6)
        self.save_table = CheckBox(frame, 'Сохранить таблицу', 7)
        self.options = ComboBox(frame, 'Действия с графиком', 8,
                                ["Показать", "Сохранить в файл", "Показать и сохранить", "Игнорировать"])
        self.error = Text(frame, self.text_error, 9)
        submit = tk.Button(frame, text='Табулировать', command=self.on_submit_click)
        submit.grid(row=10, column=2)
        window.mainloop()

    def get_values(self):
        return {
            'start': float(self.start.variable.get()),
            'end': float(self.end.variable.get()),
            'step': float(self.step.variable.get()),
            'show_table': self.show_table.variable.get(),
            'save_table': self.save_table.variable.get(),
            'option': self.options.variable.get()
        }

    def is_fields_valid(self):
        for field in [self.start, self.end, self.step]:
            if not field.valid:
                self.text_error = field.error
                return False

        if float(self.start.variable.get()) > float(self.end.variable.get()):
            self.text_error = 'Начальное значение не может быть больше конечного'
            return False
        self.text_error = ''
        return True

    def on_submit_click(self):
        if self.is_fields_valid():
            current_values = self.get_values()
            self.submit_callback(current_values)
        else:
            messagebox.showerror(title='Ошибка!', message='Введены недопустимые значения!')

    def update_error_field(self):
        self.is_fields_valid()
        self.error.text_var.set(self.text_error)
