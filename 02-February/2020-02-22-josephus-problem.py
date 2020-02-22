import sys

def start_p():
  print("Learn about this problem at https://en.wikipedia.org/wiki/Josephus_problem")
  print("Enter q to quit.")
  input_number = input("How many soliders are we talking about here? --> ")
  # test input right away
  _check_if_quit(input_number.lower())
  # next
  check_input(input_number)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_number):
  if int(input_number) > 2 and int(input_number) < 1001:
    lets_get_killing(int(input_number))
  else:
    _check_if_quit("q", "Invalid input.")

def lets_get_killing(input_number):
  number_in_binary = bin(input_number)
  number_in_binary_string = str(number_in_binary)
  place_to_stand = _calc_place_to_stand(number_in_binary_string)
  print(f"To be the last standing in a group of {input_number}, a person should stand in spot {place_to_stand}.")

def _calc_place_to_stand(number_in_binary_string):
  # cut leading 0b, move first digit to end
  place_to_stand = number_in_binary_string[3:] + number_in_binary_string[2]
  return int(place_to_stand, 2)

# call on load
start_p()