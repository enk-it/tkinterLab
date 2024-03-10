from components.Form import Form
from components.Output import Output
from utils.tabulate import getDataToPrint
from utils.tabulate import table_to_str
from utils.tabulate import get_plot


def main(values):
    start, end, delta = values["start"], values["end"], values["step"]
    table, maxlen = getDataToPrint(start, end, delta)
    table_str = table_to_str(table, maxlen)

    show_table, save_table, option = values["show_table"], values["save_table"], values["option"]

    figure, ax = get_plot(start, end, delta, table)

    if save_table:
        pass
    if option in ["Показать и сохранить", "Сохранить в файл"]:
        pass

    if show_table or option in ["Показать", "Показать и сохранить"]:
        Output(table_str, figure, show_table, option in ["Показать", "Показать и сохранить"])


Form(main)
