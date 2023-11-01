operator_list = ['+', '-', '*', '/']

def operate(operator, x, y):
  result = "Error"
  if operator == operator_list[0]:
    result = x + y
  elif operator == operator_list[1]:
    result = x - y
  elif operator == operator_list[2]:
    result = x * y
  elif operator == operator_list[3]:
    if y == 0:
      print("You cannot divide by Zero.")
    else:
      result = x / y
  return result

def PrintResults(operator, x, y, result):
  print(str(x) + " " + operator + " " + str(y) + " = " + str(answer))

valid_operator = False
valid_x = False
valid_y = False
while valid_operator == False:
  print("Operator List: ", operator_list)
  operator = input("Choose an operator from the list.")
  if operator in operator_list:
    valid_operator = True
    while valid_x == False:
      input_x = input("First Num: ")
      try:
        x = int(input_x)
      except ValueError:
        print("Input must be an integer.")
      else:
        valid_x = True
    while valid_y == False:
      input_y = input("Second Num: ")
      try:
        y = int(input_y)
      except ValueError:
        print("Input must be an integer.")
      else:
        valid_y = True
  else:
    print("Not a valid operator.")

answer = operate(operator, x, y)
PrintResults(operator, x, y, answer)