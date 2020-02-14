import sys

def start_p():
  print("Enter q to quit.")
  input_string = input("Enter numbers, separated by commas, to find the least common multiple. --> ")
  # test input right away
  _check_if_quit(input_string.lower())
  keys = _make_input_into_list(input_string)
  # next
  find_gcd_and_lcm(keys)

def _check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    exit(0)

def _make_input_into_list(input_string):
  input_list = input_string.split(",")
  result_list = []
  for item in input_list:
    result_list.append(int(item))
  return result_list

def find_gcd_and_lcm(keys):
  # I know this code is WET; I want to see explicitly what's going on to get it started.
  # first loop
  x = keys[0]
  y = keys[1]
  gcd = _gcd(x, y)
  lcm = _lcm(x, y, gcd)
  print(_output_string(x, y, gcd, lcm))

  tempLCM = lcm
  tempGCD = gcd

  # once set up, get all others
  for i in range(2, len(keys)):
    x = tempLCM
    y = keys[i]
    gcd = _gcd(x, y)
    lcm = _lcm(x, y, gcd)
    print(_output_string(x, y, gcd, lcm))
    tempLCM = lcm
    tempGCD = gcd

  # next
  output_results(keys, tempLCM)

# from a wonderful coder at https://stackoverflow.com/a/18944210
def _gcd(x, y):
  while y != 0:
    (x, y) = (y, x % y)
  return x

def _lcm(x, y, gcd):
  mult = x * y
  lcm = mult / gcd
  return int(lcm)

def _output_string(x, y, gcd, lcm):
  return "The gcd of "+str(x)+" and "+str(y)+" is "+str(gcd)+". This makes its lcm " + str(lcm) + "."

def output_results(keys, lcm):
  temp = []
  for x in keys:
    temp.append(str(x))
  output_string = ", ".join(temp)
  print("\t\tThe lowest common multiple of " + output_string + " is " + str(lcm) + ".")


######NOTES######
  # gcd testing done here: http://www.alcula.com/calculators/math/gcd/
  # lcm testing done here: https://www.calculatorsoup.com/calculators/math/lcm.php
  # changed from a prime-based strategy based on this: https://www.mathportal.org/calculators/numbers-calculators/gcd-lcm-calculator.php

# call on load
start_p()
