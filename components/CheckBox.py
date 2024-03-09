import tkinter as tk
from tkinter import ttk


class CheckBox:
	def __init__(self, frame, text, row):
		self.variable = tk.IntVar()
		self.variable.trace('w', self.callback)
		enabled_checkbutton = ttk.Checkbutton(frame, text=text, variable=self.variable)
		enabled_checkbutton.grid(row=row, column=2)


	def callback(self, *args):
		pass

