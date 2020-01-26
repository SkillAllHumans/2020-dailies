# https://stackoverflow.com/a/1058727
import random
import sys

# set variables
# colors https://en.wikipedia.org/wiki/Roulette
red = ["1", "3", "5", "7", "9", "12",
"14", "16", "18", "19", "21", "23",
"25", "27", "30", "32", "34", "36"]
black = ["2", "4", "6", "8", "10", "11",
"13", "15", "17", "20", "22", "24",
"26", "28", "29", "31", "33", "35"]
green = ["0", "00"]
numbers = red + black + green
evens = ["0","2","4","6","8","10","12","14","16","18","20","22","24","26","28","30","32","34","36"]
odds = ["1","3","5","7","9","11","13","15","17","19","21","23","25","27","29","31","33","35"]
part1 = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
part2 = ["19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36"]
choices = {"1": red, "2": black, "3": green, "4": evens, "5": odds, "6": part1, "7": part2}
modifiers = {"1": 1, "2": 1, "3": 17, "4": 1, "5": 1, "6": 1, "7": 1}

def start_p():
  print("Enter a single q to quit program.\n\nYour bank starts at $500.")
  bank = 500
  start_round(bank)

def start_round(bank=500):
  # get choice
  input_choice = input("Enter a number to choose.\n\t1) red\n\t2) black\n\t3) green\n\t4) evens\n\t5) odds\n\t6) 1 to 18\n\t7) 19-36\n\tYour choice --> ")
  check_if_quit(input_choice)
  # get user bet
  input_bet = input("Enter your bet ($1-max bank) --> ")
  check_if_quit(input_bet)
  # next steps
  check_user_choice(input_choice, input_bet, bank)

def error_p(text="Error. Try again."):
  print(text)
  start_p()

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    exit(0)

def check_user_choice(input_choice, input_bet, bank):
  try:
    val = int(input_choice)
    if val < 1 or val > 7:
      error_p("Choose from 1 to 7.")
    val2 = int(input_bet)
    val3 = int(bank)
    if val2 < 2 or val2 > val3:
      error_p("Choose from 1 to max bank.")
    spin_wheel(input_choice, input_bet, bank)
  except:
    error_p()

def spin_wheel(val, bet, bank):
  lands_on = str(random.choice(numbers))
  chosen_array = choices[val]
  tf = False
  if lands_on in chosen_array:
    tf = True
  adjust_bank(val, bet, bank, lands_on, tf)
  

def adjust_bank(val, bet, bank, lands_on, tf):
  results = int(bet) * int(modifiers[val])
  if tf == True:
    bank += int(results)
  else:
    bank -= int(bet)
  print("You chose " + str(choices[val]) + "\n and the winning number was " + str(lands_on) + ".\n Your bank is " + str(bank) + ".")
  see_if_continue(val, bank, lands_on)

def see_if_continue(val, bank, lands_on):
  if bank < 1:
    print("Sorry, you're bust!")
  else:
    check_cash_out(bank)

def check_cash_out(bank):
  cash_out = input("Hit c to cash out --> ")
  if cash_out.lower() != "c" and cash_out.lower() != "q":
    start_round(bank)
  else:
    print("You're walking away with " + str(bank) + "!")

# kick things off
start_p()
