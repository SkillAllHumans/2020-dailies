import sys
import random

#globals
deck = ["♣A", "♣K", "♣Q", "♣J", "♣10", "♣9", "♣8", "♣7", "♣6", "♣5", "♣4", "♣3", "♣2",
"♦A", "♦K", "♦Q", "♦J", "♦10", "♦9", "♦8", "♦7", "♦6", "♦5", "♦4", "♦3", "♦2",
"♥A", "♥K", "♥Q", "♥J", "♥10", "♥9", "♥8", "♥7", "♥6", "♥5", "♥4", "♥3", "♥2",
"♠A", "♠K", "♠Q", "♠J", "♠10", "♠9", "♠8", "♠7", "♠6", "♠5", "♠4", "♠3", "♠2"]

def start_p():
  print("Enter q to quit.")
  input_number = input("How many cards do you want? --> ")
  # test input right away
  _check_if_quit(input_number.lower())
  # next
  check_input(input_number)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_number):
  # is int?
  if type(int(input_number)) == int and int(input_number) != 0 and int(input_number) > 0  and int(input_number) < 53:
    random.shuffle(deck)
    cards = _get_cards(int(input_number))
    # output
    print(f" The shuffled deck is {', '.join(deck)}.\n\n\t Your cards are {', '.join(cards)}.")
  else:
    _check_if_quit("q", "Invalid input.")

def _get_cards(input_number):
  cards = []
  x = 0
  while x < input_number:
    cards.append(deck[x])
    x += 1
  return cards

# call on load
start_p()