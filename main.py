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
    show_plot = option in ["Показать", "Показать и сохранить"]
    figure, ax = get_plot(start, end, delta, table)

    if save_table:
        with open('table.txt', 'w') as file:
            file.write(table_str)
    if option in ["Показать и сохранить", "Сохранить в файл"]:
        figure.savefig('Graph')

    Output(table_str, figure, show_table, show_plot)


Form(main)
