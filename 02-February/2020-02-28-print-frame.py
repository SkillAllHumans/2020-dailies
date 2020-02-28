import sys

def start_p():
  print("Enter q to quit.")
  input_string = input("Enter the string you want displayed in a frame. --> ")
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
    make_frame(input_string.split())
  else:
    _check_if_quit("q", msg = "Check your string length.")

def make_frame(input_array):
  print("*" * 80)
  for x in input_array:
    spaces = _make_spaces(x)
    temp = (int(spaces)*" ") + x + (int(spaces)*" ")
    if len(temp) < 76:
      temp += " "
    print(f"**{temp}**")
  print("*" * 80)

def _make_spaces(x):
  spaces = (76 - len(x))
  if spaces % 2 == 0:
    spaces /= 2
  else:
    spaces = (spaces - 1) / 2
  return spaces

# call on load
start_p()