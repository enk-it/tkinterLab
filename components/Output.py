import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


class Output:
    def __init__(self, table_str, figure, show_table, show_plot):
        if not (show_plot or show_table):
            return
        self.window = tk.Tk()
        self.window.title("Вывод результата табуляции")
        self.window.geometry("1024x800")

        if show_plot:
            self.show_plot(figure)
        if show_table:
            self.show_table(table_str)

    def show_table(self, table_str):
        text = ScrolledText(master=self.window)
        text.insert(1.0, table_str)
        text.tag_configure("center", justify='center')
        text.tag_add("center", "1.0", "end")
        text.config(state=tk.DISABLED)
        text.pack()

    def show_plot(self, figure):
        canvas = FigureCanvasTkAgg(figure,
                                   master=self.window)
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas,
                                       self.window)
        toolbar.update()
        canvas.get_tk_widget().pack()

