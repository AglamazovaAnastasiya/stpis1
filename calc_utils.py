def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Ошибка! Введите число")

def show_welcome():
    print("=== КАЛЬКУЛЯТОР ===")
    print("Добро пожаловать!")

def show_menu():
    print("\n=== МЕНЮ ===")
    print("1. Сложение")
    print("2. Вычитание") 
    print("3. Умножение")
    print("4. Деление")
    print("5. Выход")
