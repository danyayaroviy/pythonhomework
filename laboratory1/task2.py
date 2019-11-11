print("Лабораторна робота №1 Варіант 24")
print("Виконав студент групи КМ-93")
print("Яровий Данило Євгенійович")
print("Завдання 2")
import re
def floatpositive_input(text):
    pattern = "^\d*(\.\d+)?$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне, введіть додатнє раціональне число:")
    return float(user_input)

end = ""
while end != "1":
    a = floatpositive_input("Введіть довжину першої сторони:")
    b = floatpositive_input("Введіть довжину другої сторони: ")
    c = floatpositive_input("Введіть довжину третьої сторони: ")
    if a<(b+c) and b<(a+c) and c<(a+b):
        print("Такий трикутник існує")
    else:
        print("Такий трикутник не існує")
    end = input("Введіть 1 для завершення або будь-що інше для продовження")