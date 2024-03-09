from components.Form import Form
from utils.tabulate import getDataToPrint
from utils.tabulate import table_to_str
from utils.tabulate import show_graph





def main(values):
	start, end, delta = values["start"], values["end"], values["step"]
	graph, options = values["graph"], values["options"]
	table, maxlen = getDataToPrint(start, end, delta)

	table_str = table_to_str(table, maxlen)
	print(table_str)

	show_graph(start, end, delta, table)


Form(main)




