import sys

def start_p():
  print("Enter q to quit.")
  input_string = input("Enter the string you want displayed diagonally --> ")
  # test input right away
  _check_if_quit(input_string.lower())
  # next
  check_input(input_string)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_string):
  if len(input_string) > 1 and len(input_string) < 500:
    spacing = 0
    for x in input_string:
      if spacing > 80:
        spacing = 0
      else:
        spacing += 1
      spaces = " " * spacing
      print(f"{spaces}{x}")
  else:
    _check_if_quit("q", msg = "Check your string length.")

# call on load
start_p()