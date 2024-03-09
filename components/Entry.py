import tkinter as tk
from tkinter import ttk
from utils.validate import validate_float



class Entry:
	def __init__(self, frame, text, row):

		self.variable = tk.StringVar()
		self.variable.trace('w', self.onChange)

		self.start_label = tk.Label(frame, text=text)
		self.start_label.grid(row=row, column=1)
		self.start_entry = tk.Entry(frame, textvariable=self.variable)
		self.start_entry.grid(row=row, column=2)

		self.valid = False

	def onChange(self, *args):
		value = self.variable.get()
		self.validate(value)

	def validate(self, value):
		if validate_float(value):
			self.valid = True
			self.start_entry.configure(background='white')
		else:
			self.valid = False
			if value == '':
				self.start_entry.configure(background='white')
			else:
				self.start_entry.configure(background='red')

