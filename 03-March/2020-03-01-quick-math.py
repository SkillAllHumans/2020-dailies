import sys

# globals
digits = "0123456789"

def start_p():
  print("Enter q to quit.")
  input_string = input("Enter the number you want analyzed (separated by commas). --> ")
  _check_if_quit(input_string.lower())
  input_sign = input("Enter the sign of the operation you want to do (+, -, *, /). -- >")
  _check_if_quit(input_sign.lower())
  # next
  check_input(input_string, input_sign)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_string, input_sign):
  if input_sign == "+" or input_sign == "-" or input_sign == "*" or input_sign == "/":
    analyze_string(input_string, input_sign)
  else:
    _check_if_quit("q", msg = "Check your string length.")

def analyze_string(input_string, input_sign):
  # strip spaces
  input_array = _get_numbers_only("".join(input_string.split()))
  result_string = ""
  for x in input_array:
    result_string += (x + input_sign)
  print(result_string[:-1])
  result_number = eval(result_string[:-1])
  print(f"Your request for {result_string[:-1]} evaluates to {result_number}.")

def _get_numbers_only(input_string):
  input_array = input_string.split(",")
  number_array = []
  for item in input_array:
    temp = ""
    for char in item:
      if char in digits:
        temp += char
    number_array.append(temp)
  return number_array

# call on load
start_p()