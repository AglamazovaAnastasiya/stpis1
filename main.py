from calc_operations import *
from calc_utils import *

while True:
    show_menu()
    choice = input("Выберите действие: ")
    
    if choice == "5":
        print("Пока!")
        break
    
    if choice in ["1", "2", "3", "4"]:
        a = get_number("Первое число: ")
        b = get_number("Второе число: ")
        
        if choice == "1":
            result = add(a, b)
            print(f"Результат: {a} + {b} = {result}")
        elif choice == "2":
            result = subtract(a, b)
            print(f"Результат: {a} - {b} = {result}")
        elif choice == "3":
            result = multiply(a, b)
            print(f"Результат: {a} * {b} = {result}")
        elif choice == "4":
            if b == 0:
                print("Ошибка: на ноль делить нельзя!")
            else:
                result = divide(a, b)
                print(f"Результат: {a} / {b} = {result}")
    else:
        print("Неверный выбор!")
