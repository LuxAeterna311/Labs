import math


def function(x):
	y = math.tan(x) + 2 * math.sin(x)
	return y


def main():
	a = float(input("Введите начало отрезка: "))
	b = float(input("Введите конец отрезка: "))
	eps = float(input("Введите точность: "))


	phi = (1 + 5 ** (0.5)) / 2

	while (abs(a - b) > eps):
		x1 = b - (b - a) / phi
		x2 = a + (b - a) / phi

		y1 = function(x1)
		y2 = function(x2)

		if y1 >= y2:
			a = x1
		else:
			b = x2

	print((a + b) / 2)


if __name__ == "__main__":
	main()
else:
	print("Файл не является подключаемым, только исполняемым!")