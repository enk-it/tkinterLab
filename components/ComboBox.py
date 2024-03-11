import tkinter as tk
from tkinter import ttk


class ComboBox:
    def __init__(self, frame, text, row, options):
        self.variable = tk.StringVar()
        self.variable.set(options[0])

        table_label = tk.Label(frame, text=text)
        table_label.grid(row=row, column=1)
        combobox = ttk.Combobox(frame, state="readonly", values=options, textvariable=self.variable)
        combobox.grid(row=row, column=2)

