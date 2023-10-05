operator_list = ["+", "-", "*", "/"]

while True:
    operator = input("Choose an operation (+ - * /): ")
    if operator in operator_list:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        if operator == operator_list[0]:
            result = x+y
            print(f"{x} + {y} = {result}")
            break
        elif operator == operator_list[1]:
            result = x-y
            print(f"{x} - {y} = {result}")
            break
        elif operator == operator_list[2]:
            result = x*y
            print(f"{x} * {y} = {result}")
            break
        elif operator == operator_list[3]:
            try:
                result = x / y
                print(f"{x} / {y} = {result}")
                break
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                break
    else:
        print("Invalid input. Choose an operation (+ - * /): ")
