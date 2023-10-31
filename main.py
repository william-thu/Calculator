operator_list = ["+", "-", "*", "/"]

def calculate(operator, firstnum, secondnum):
    while True:
        if operator == operator_list[0]:
            result = firstnum + secondnum
            print(f"{firstnum} + {secondnum} = {result}")
            break
        elif operator == operator_list[1]:
            result = firstnum - secondnum
            print(f"{firstnum} - {secondnum} = {result}")
            break
        elif operator == operator_list[2]:
            result = firstnum * secondnum
            print(f"{firstnum} * {secondnum} = {result}")
            break
        elif operator == operator_list[3]:
            try:
                result = firstnum / secondnum
                print(f"{firstnum} / {secondnum} = {result}")
                break
            except ZeroDivisionError:
                print("Cannot divide by zero.")
                break

valid_operator = False
while valid_operator == False:
    operator = input("Choose an operation (+ - * /): ")
    if operator in operator_list:
        valid_operator = True
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))

    else:
        print("Invalid input. Choose an operation (+ - * /): ")

calculate(operator, x, y)