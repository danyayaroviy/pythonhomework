print("Лабораторна робота №2 Варіант 24")
print("Виконав студент групи КМ-93")
print("Яровий Данило Євгенійович")
print("Завдання 2")
import re
def int_input(text):
    pattern = r"^[-\d]\d*$"
    user_input = input(text)

    while not re.match(pattern, user_input):
        user_input = input("Введіть ціле число")
    return int(user_input)
i = 0
max_int = 0
a = 0
b = 0

end = ""
while end != "1":
    a = int_input("Будь ласка, введіть перше значення (А): ")
    b = int_input("Будь ласка, введіть друге значення (В): ")
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    print("\nНайбільший спільний дільник чисел А і В дорівнює " + str(a + b))
    end = input("Введіть 1 для завершення або будь-що інше для продовження")
