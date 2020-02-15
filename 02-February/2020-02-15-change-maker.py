import sys

def start_p():
  print("Enter q to quit.")
  input_string = input("Enter the amount of (American) money you need to pay out --> ")
  # test input right away
  _check_if_quit(input_string.lower())
  # next
  check_input(input_string)

def _check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    exit(0)

def check_input(input_string):
  if input_string.count(".") == 1:
    dollars, change = input_string.split(".")
    d, c = int(dollars), int(change[:2])
    if d and c:
      make_change(d, c)
  else:
    _check_if_quit("q")

def _dollars_into_bills(dollars):
  bills_val = [100, 50, 20, 10, 5, 1]
  bills_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}

  for bill in bills_val:
    temp = dollars // bill
    bills_dict[bill] = temp
    dollars -= temp*bill

  return bills_dict

def _change_into_coins(change):
  coins_val = [25, 10, 5, 1]
  coins_dict = {25: 0, 10: 0, 5: 0, 1: 0}

  for coin in coins_val:
    temp = change // coin
    coins_dict[coin] = temp
    change -= temp*coin

  return coins_dict

def make_change(dollars, change):
  bills_dict = _dollars_into_bills(dollars)
  coins_dict = _change_into_coins(change)
  output_results(dollars, change, bills_dict, coins_dict)


def output_results(dollars, change, bills_dict, coins_dict):
  text = "The best way to pay out $"+str(dollars)+"."+str(change)+" is:\n"
  bills_string, coins_string = "", ""
  for k, v in bills_dict.items():
    if v != 0:
      bills_string += "\t(" + str(v) + ") $" + str(k) + " bills\n"

  for k, v in coins_dict.items():
    if v != 0:
      coins_string += "\t(" + str(v) + ") " + str(k) + "¢ coins\n"

  print(text, bills_string, coins_string)

# call on load
start_p()
