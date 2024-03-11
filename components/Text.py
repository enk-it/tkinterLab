import tkinter as tk


class Text:
    def __init__(self, frame, text, row):
        self.text_var = tk.StringVar()
        self.text_var.set(text)
        label = tk.Label(frame, textvariable=self.text_var)
        label.grid(row=row, column=1)
