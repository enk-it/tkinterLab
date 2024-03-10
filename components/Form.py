import tkinter as tk
from tkinter import messagebox
from components.Entry import Entry
from components.CheckBox import CheckBox
from components.ComboBox import ComboBox
from components.Output import Output

class Form:
    def __init__(self, submit_callback):
        self.submit_callback = submit_callback
        window = tk.Tk()

        window.attributes('-type', 'utility ')

        window.title("Табулирование функций tkinter")
        window.geometry("800x600")

        label = tk.Label(window, text="Функция y = f(x)")
        label.pack()

        frame = tk.Frame(window, padx=10, pady=10)
        frame.pack(expand=True)

        self.start = Entry(frame, 'Введите начальное значение', 3)
        self.end = Entry(frame, 'Введите конечное значение', 4)
        self.step = Entry(frame, 'Введите значение шага', 5, strict_positive=True)
        self.show_table = CheckBox(frame, 'Показать таблицу', 6)
        self.save_table = CheckBox(frame, 'Сохранить таблицу', 7)
        self.options = ComboBox(frame, 'Действия с графиком', 8,
                                ["Показать", "Сохранить в файл", "Показать и сохранить", "Игнорировать"])

        submit = tk.Button(frame, text='Табулировать', command=self.on_submit_click)
        submit.grid(row=9, column=2)
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
