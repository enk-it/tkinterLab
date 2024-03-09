import tkinter as tk
from tkinter import ttk
from utils.validate import validate_float



class Entry:
	def __init__(self, frame, text, row, strict_positive=False):
		self.strict_positive = strict_positive

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
		if value == '':
			self.valid = False
			self.start_entry.configure(background='white')
		elif not validate_float(value):
			self.valid = False
			self.start_entry.configure(background='red')
		elif self.strict_positive and float(value) <= 0:
			self.valid = False
			self.start_entry.configure(background='red')
		else:
			self.valid = True
			self.start_entry.configure(background='white')

