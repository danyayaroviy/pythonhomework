print("Лабораторна робота №2 Варіант 24")
print("Виконав студент групи КМ-93")
print("Яровий Данило Євгенійович")
print("Завдання 1")
import re

def int_input():
    pattern = r"^\d*$"
    user_input = input()

    while not re.match(pattern, user_input):
        user_input = input("Введіть натуральне число:")
    return int(user_input)
def float_input():
    pattern1 = "^-?\d+(\.\d+)?$"
    user_input = input()

    while not re.match(pattern1, user_input):
        user_input = input("Введіть раціональне число:")
    return float(user_input)
end = ""
while end != "1":
    n = 0
    x = 0
    while n < 1:
        try:
            print("Введіть значення верхньої межі сумування: ")
            n = int_input()
            break
        except ValueError:
            print("Верхня межа сумування повинна бути додатньою та цілою.")
            print("Введіть інше значення: ")
            n = int_input()
    while 1:
         try:
             print("Введіть значення x: ")
             x = float_input()
             break
         except ValueError:
             print("Введіть числове значення x: ")
             x = float_input()
    s = 0
    for i in range(n):
        s= s + (x**(i+1)+n)/(x-n)
    print("Сумма дорівнює " + str(s))
    end = input("Введіть 1 для завершення або будь-що інше для продовження")