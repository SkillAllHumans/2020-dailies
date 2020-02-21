import sys
import random

def start_p():
  print("Enter q to quit.")
  input_door = input("Pick a door. You have a 1 in 3 chance of being right. Enter 1, 2, or 3. --> ")
  # test input right away
  _check_if_quit(input_door.lower())
  # next
  check_input(input_door)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_door):
  if input_door != str(1) and input_door != str(2) and input_door != str(3):
    _check_if_quit("q", "Invalid input.")
  else:
    play_the_game(int(input_door))

def play_the_game(input_door):
  doors_and_prizes_dict = _make_doors_dictionary()
  prize_door, opened_door, closed_door = _assign_doors(doors_and_prizes_dict, input_door)
  user_choice = _chance_to_change_door(opened_door, input_door)
  user_win, choice_door = False, input_door
  if user_choice:
    choice_door = closed_door
  if choice_door == prize_door:
    user_win = True
  _end_the_game(choice_door, closed_door, prize_door, doors_and_prizes_dict, user_win)

def _make_doors_dictionary():
  prizes = ["goat", "car", "goat"]
  #make random
  random.shuffle(prizes)
  doors_and_prizes_dict = {1: prizes[0], 2: prizes[1], 3: prizes[2]}
  return doors_and_prizes_dict

def _assign_doors(doors_and_prizes_dict, input_door):
  prize_door, opened_door, closed_door = 1, 1, 1
  for k, v in doors_and_prizes_dict.items():
    if v == "goat" and k != input_door:
      opened_door = k
    if v == "car":
      prize_door = k
  for k, v in doors_and_prizes_dict.items():
    if k != opened_door and k != input_door:
      closed_door = k
  return prize_door, opened_door, closed_door

def _chance_to_change_door(opened_door, input_door):
  print(f"You've chosen Door {input_door}. Monty opens Door {opened_door}, showing you a goat.\nThere was a 1 in 3 chance for each of the two doors you didn't choose that it would have the car.\nNow, Monty has shared with you that one of those doors has a goat.\nThe odds are still 1 in 3 that you guessed correctly and 2 in 3 that you didn't.\nHOWEVER, the odds are also now 2 in 3 that the other remaining door has the car.")
  user_choice = input(f"\n\tWill you switch? (y/n) --> ")
  if user_choice.lower() == "y" or user_choice.lower() == "yes":
    print("You've chosen to switch doors.")
    return True
  else:
    print("You've chosen not to switch doors.")
    return False
  
def _end_the_game(choice_door, closed_door, prize_door, doors_and_prizes_dict, user_win):
  print(f"Your choice is Door {choice_door}.\nMonty opens Door {closed_door}, revealing a {doors_and_prizes_dict[closed_door]}.")
  if user_win:
    print(f"The car is behind {prize_door}! You win.")
  else:
    print(f"The car is behind {prize_door}! You lose.")
# call on load
start_p()