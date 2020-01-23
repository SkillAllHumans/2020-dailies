# https://stackoverflow.com/a/1058727
import random
import sys

def start_p():
  print("Enter a single q to quit program.")
  input_sides = input("How many sides (from 6-40) does your die have? --> ")
  check_if_quit(input_sides)
  input_times = input("How many times (1-100) do you want to roll the die? --> ")
  check_if_quit(input_times)

  check_user_choice(input_sides, input_times)

def quit_p():
  exit(0)

def error_p(text="Error. Try again."):
  print(text)
  start_p()

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    quit_p()

def check_user_choice(input_sides, input_times):
  try:
    val1 = int(input_sides)
    val2 = int(input_times)
    if val1 < 6 or val1 > 40:
      error_p("Sides must be from 6-40")
    if val2 < 1 or val2 > 100:
      error_p("Times must be from 1-100")
    roll_die(val1, val2)
  except:
    error_p()

def roll_die(sides, times):
  for i in range(int(times)):
    roll = random.randint(1,int(sides))
    print("Roll " + str(i+1) + " is: " + str(roll))

start_p()
