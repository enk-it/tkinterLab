import math
import matplotlib.pyplot as plt

def show_graph(start, end, delta, table):
	title = f"""График функции y = f(x)
	В промежутке от {start} до {end} с шагом {delta}"""

	x1 = []
	y1 = []


	for x in table:
		value = table[x]
		x1.append(x)
		y1.append(value)


	plt.plot(x1, y1, label='f(x)', color='red')


	plt.xlim(-3, 3)
	plt.ylim(-3, 3)

	ax = plt.gca()
	ax.set_aspect('equal', adjustable='box')

	plt.xlabel("X")
	plt.ylabel("Y")
	plt.legend()
	plt.grid()
	plt.title(title)
	plt.show()


def getMax(list):
	result = None

	for i in list:
		if result is None or i > result:
			result = i

	return result


def f(x):
	if x != 0:
		return (-x)/((x ** 5) * (math.e ** math.sin(x)))


def getDataToPrint(start, end, delta):
	max_len = -1
	i = 0
	result = {}

	if delta > 0:
		while start + delta * i <= end:
			x = start + delta * i
			if x != 0:
				y = f(x)
				result[round(x, 3)] = round(y, 3)
				max_len = getMax([max_len, len(str(x)), len(str(result[round(x, 3)]))])
			i += 1
	else:
		while start + delta * i >= end:
			
			x = start + delta * i
			if x != 0:
				y = f(x)
				result[round(x, 3)] = round(y, 3)
				max_len = getMax([max_len, len(str(x)), len(str(result[round(x, 3)]))])
			i += 1
	return result, max_len



def table_to_str(table, maxlen):
	result = ""

	maxlen += 4

	result += '+' + '-' * (maxlen * 2 + 1) + "+" + '\n'
	result += "|" + str("x").center(maxlen) + "|" + str('f(x)').center(maxlen) + "|" + '\n'
	result += '+' + '-' * (maxlen * 2 + 1) + "+" + '\n'
	for x in table:
		result += "|" + str(x).center(maxlen) + "|" + str(table[x]).center(maxlen) + "|" + '\n'
		result += '+' + '-' * (maxlen * 2 + 1) + "+" + '\n'
	return result