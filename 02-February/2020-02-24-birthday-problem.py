import sys

def start_p():
  print("Learn about this problem at https://en.wikipedia.org/wiki/Birthday_problem")
  print("Enter q to quit.")
  input_number = input("How many people are we talking about here? --> ")
  # test input right away
  _check_if_quit(input_number.lower())
  # next
  check_input(int(input_number))

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_number):
  if input_number > 2 and input_number < 367:
    birthday_probability = _get_birthday_odds(input_number, 365.00)
    birthday_probability_leap = _get_birthday_odds(input_number, 365.25)
    print(f"With a group of {input_number}, there's a birthday probability of approximately {birthday_probability}%.")
    print(f"Including leap years, there's a birthday probability of approximately {birthday_probability_leap}%.")
  else:
    _check_if_quit("q", "Invalid input.")

def _get_birthday_odds(input_number, factor):
  inverse_odds = 1
  for x in range(1, input_number):
    inverse_odds *= ((factor - int(x)) / factor)
  return (1 - inverse_odds) * 100

# call on load
start_p()