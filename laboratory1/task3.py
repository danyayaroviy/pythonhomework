print("Лабораторна робота №1 Варіант 24")
print("Виконав студент групи КМ-93")
print("Яровий Данило Євгенійович")
print("Завдання 1") 
import re
def floatpositive_input(text):
    pattern = "^\d*(\.\d+)?$"
    user_input = input(text)
    while not re.match(pattern, user_input):
        user_input = input("Введене значення некоректне, введіть додатнє раціональне число:")
    return float(user_input)
end = ""
while end != "1":
    r1 = floatpositive_input("Введіть перший опір (Ом): ")
    r2 = floatpositive_input("Введіть другий опір (Ом): ")
    r3 = floatpositive_input("Введіть третій опір (Ом): ")

    r = round((1/((1/r1)+(1/r2)+(1/r3))), 2)

    print("Загальний опір дорівнює ", str(r), " Ом")
    end = input("Введіть 1 для завершення або будь-що інше для продовження")