import sys

def start_p():
  print("Enter q to quit.")
  input_type = input("Is your temperature Fahrenheit, Celsius, Kelvin, or Rankine (f, c, k, r)? --> ")
  input_number = input("What is your temperature number? --> ")
  input_desired_type = input("Which temperature are you converting to (f, c, k, r) ? --> ")
  # test input right away
  _check_if_quit(input_number.lower())
  # next
  check_input(float(input_number), input_type, input_desired_type)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_number, input_type, input_desired_type):
  # check for equal types
  if input_type == input_desired_type:
    _check_if_quit("q", "Nothing to convert.")
  # limit input
  if input_number > -100 and input_number < 500:
    # standardize everything
    if input_type == "f" or input_type == "k" or input_type == "r":
      result_number = _convert_to_c(input_number, input_type)
      print(result_number)
    else:
      result_number = input_number
    # get result unit
    if input_desired_type == "c":
      final_conversion = result_number
    else:
      final_conversion = _final_conversion(result_number, input_desired_type)
    print(f"{input_number} in {input_type} is approximately {final_conversion} in {input_desired_type}.")
  else:
    _check_if_quit("q", "Invalid input.")

def _convert_to_c(input_number, input_type): 
  if input_type == "f":
    return (input_number - 32 ) * (5/9)
  elif input_type == "k":
    return (input_number - 273.15)
  else:
    return (input_number - 491.67) * (5/9)

def _final_conversion(result_number, input_desired_type):
  if input_desired_type == "f":
    return result_number * (9/5) + 32
  elif input_desired_type == "k":
    return result_number + 273.15
  else:
    return (result_number + 273.15) * (9/5)

# call on load
start_p()