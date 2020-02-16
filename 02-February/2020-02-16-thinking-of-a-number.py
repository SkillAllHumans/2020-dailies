import sys
from random import randint

def start_p():
  print("Enter q to quit.")
  comp_number = randint(1, 10) #inclusive of 10
  guess(0, comp_number, 0)

def guess(input_number, comp_number, guess_count):
  input_number = input("Enter a number between 1 and 10 --> ")
  # test input right away
  _check_if_quit(input_number.lower())
  if int(input_number) > 0 or int(input_number) < 11:
    # next
    narrow_hints(int(input_number), comp_number, guess_count)
  else:
    _check_if_quit("q", "Input a number")

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)


def narrow_hints(input_number, comp_number, guess_count):
  input_number = int(input_number)
  comp_number = int(comp_number)
  guess_count = int(guess_count)

  guess_count += 1

  if input_number == comp_number:
    output_results(input_number, comp_number, guess_count)
  elif input_number < comp_number:
    print("Guess higher.")
    guess(input_number, comp_number, guess_count)
  elif input_number > comp_number:
    print("Guess lower.")
    guess(input_number, comp_number, guess_count)
  else:
    _check_if_quit("q", "Input a numfdfdber.")


def output_results(input_number, comp_number, guess_count):
  text = "It took "+str(guess_count)+" guess for you to find out that I was thinking of "+str(comp_number)+"!"
  print(text)

# call on load
start_p()
