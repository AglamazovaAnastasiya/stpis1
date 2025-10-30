operation_history = []

def add_to_history(operation, a, b, result):
    operation_history.append(f"{a} {operation} {b} = {result}")

def show_history():
    print("\n=== ИСТОРИЯ ОПЕРАЦИЙ ===")
    for item in operation_history:
        print(item)
