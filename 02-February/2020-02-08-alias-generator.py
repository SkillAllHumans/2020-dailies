import random
import sys

# globals
animals = ["Hawk", "Eagle", "Shark", "Hamster", "Dove", "Lion", "Eel"]
weapons = ["Katana", "Knife", "Rope", "Kick", "Dagger", "Cannon"]
adjectives = ["Blind", "Leaky", "Soft", "Cool", "Dry", "Severe", "Wide", "Narrow", "Slow"]
prefixes = ["Mc", "Mac", "Di", "De", "Del ", "De La ", "Du", "San", "St. "]
hyphenates = ["-Quickly", "-Finally", "-Butterbean", "-Shakes", "-Bones", "-Evergreen", "-Corkle"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def start_p():
  print("Generate a series of aliases for many of life's curves. Enter q to quit.")
  input_1 = input("What's your mother's maiden name? --> ")
  check_input(input_1) # test input right away
  input_2 = input("What's your first pet's name? --> ")
  check_input(input_2) # test input right away
  input_3 = input("What street did you grow up on? --> ")
  check_input(input_3) # test input right away
  input_4 = input("What's your middle name? --> ")
  check_input(input_4) # test input right away
  input_5 = input("What's your last name? --> ")
  check_input(input_5) # test input right away
  input_6 = input("Who was president when you were born? --> ")
  check_input(input_6) # test input right away

  # next
  check_user_choice(input_1.capitalize(), input_2.capitalize(), 
    input_3.capitalize(), input_4.capitalize(), 
    input_5.capitalize(), input_6.capitalize())

def check_input(choice):
  if str(choice).lower() == "q":
    print("Goodbye!")
    exit(0)
  val1 = len(choice)
  if val1 < 1 or val1 > 50:
    print("Length must be from 1 to 50.")
    exit(0)

def check_user_choice(input_1, input_2, input_3, input_4, input_5, input_6):
  try:
    make_names(input_1, input_2, input_3, input_4, input_5, input_6)
  except:
    print("here")
    exit(0)

def make_names(input_1, input_2, input_3, input_4, input_5, input_6):
  name_1 = input_1 + " \"" + random.choice(animals) + "\" " + input_6
  name_2 = input_2 + " \"The " + random.choice(weapons) + "\" " + input_1 + random.choice(hyphenates)
  name_3 = random.choice(adjectives) + " " + input_3 + " " + random.choice(weapons)
  name_4 = input_4 + " " + random.choice(letters) + ". " + random.choice(prefixes) + input_3

  print("*******************************************************************************")
  print("\t" + name_1)
  print("\t" + name_4)
  print("\t" + name_2)
  print("\t" + name_3)
  print("  These aliases will get you onto a good start in your seedy new life!")
  print("*******************************************************************************")

start_p()
