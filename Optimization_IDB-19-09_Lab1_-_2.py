import math

def function(x):
	y = math.tan(x) + 2 * math.sin(x)
	return y


def main():
	a = float(input("Введите начало отрезка: "))
	b = float(input("Введите конец отрезка: "))
	eps = float(input("Введите точность: "))

	while (abs(a - b) > eps):
		x = (a + b) / 2

		y1 = function(a)
		y2 = function(x)

		if (y1 * y2) < 0:
			b = x		
		else:
			a = x

		x = (a - b) / 2

	print(f"x: {x}. f(x): {function(x)}")


if __name__ == "__main__":
	main()
else:
	print("Файл не является подключаемым, только исполняемым!")