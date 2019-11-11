print("Лабораторна робота №1 Варіант 24")
print("Виконав студент групи КМ-93")
print("Яровий Данило Євгенійович")
print("Завдання 3")
import re
def more_than_13_input(text):
    pattern = "^\W((?!^3$).)*$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне, введіть раціональне число, що не дорівнює 3:")
    return float(user_input)

def F(x):
    if x >= 13:
        f = (-x**2-9)
    else:
        f = 1/(-x**2-9)
    print('F(x) = ', str(round(f, 2)))

end = ""
while end != "1":
    x = more_than_13_input("Введіть x: ")
    F(x)
    end = input("Введіть 1 для завершення або будь-що інше для продовження")