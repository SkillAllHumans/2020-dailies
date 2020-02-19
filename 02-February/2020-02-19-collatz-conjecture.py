import sys

def start_p():
  print("Enter q to quit.")
  input_number = input("Enter the integer, over 1, that you want to examine. --> ")
  # test input right away
  _check_if_quit(input_number.lower())
  # next
  check_input(input_number)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_number):
  if type(int(input_number)) == int and int(input_number) > 1:
    collatz_cycle(int(input_number))
  else:
    _check_if_quit("q", "Invalid input.")

def collatz_cycle(input_number):
  n = input_number
  steps = 0
  while n > 1:
    if n % 2 == 0:
      n = n/2
      print(f"{int(n*2)} divided by 2 is {int(n)}.")
    else:
      t = n
      n = ((n*3)+1)
      print(f"{int(t)} multiplied by 3, plus 1, is {int(n)}.")
    steps += 1
  print(f"It took {int(steps)} steps to get {input_number} to 1 with the Collatz conjecture.")

# call on load
start_p()