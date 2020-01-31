import sys
from functools import reduce

def start_p():
  print("Enter q at any time to quit.")
  input_number = input("Enter the number to work on (from 1-500). --> ")
  # test input right away
  check_if_quit(input_number.lower())    
  # next
  check_user_choice(input_number)

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    exit(0)

def check_user_choice(input_number):
  try:
    val1 = int(input_number)
    if val1 > 0 and val1 < 500:
      make_factorial(input_number)
    else:
      print("Enter a number between 1 and 500.")
      start_p()
  except ValueError:
     print("Enter a number between 1 and 500.")
     start_p()

def make_factorial(input_number):
  temp = int(input_number) - 1
  result = 1
  output_string = str(input_number) + "! = " +  str(input_number) + " x "
  # range options https://stackoverflow.com/a/869902
  for x in range(temp, 0, -1):
    result += x * result
    if x == 1:
      output_string += str(x) + "."
    else:
      output_string += str(x) + " x "

  print(output_string)
  print("The result is " + str(result) + ".")
  start_p()
    
# call on load
start_p()