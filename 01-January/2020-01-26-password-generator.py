# https://stackoverflow.com/a/1058727
import random
import sys
# https://stackoverflow.com/a/16060908
import string

# globals
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

choices1 = lowercase + uppercase + digits
choices2 = choices1 + punctuation

def start_p():
  print("Generate a strong password. Enter q to quit.")
  input_length = input("How long should it be? (10-100) --> ")
  # test input right away
  val1 = int(input_length)
  check_if_quit(input_length)
  if val1 < 10 or val1 > 100:
    error_p("Length must be from 10 to 100.")

  # test input right away
  input_choice = input("Error: Select:\n\t1) only alphanumeric characters\n\t2) include special characters --> ")
  check_if_quit(input_choice)
  if input_choice != "1" and input_choice != "2":
    error_p("Error: Select character types.")
    
  # next
  check_user_choice(input_length, input_choice)

def error_p(text="Error. Try again."):
  print(text)
  exit(0)

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    exit(0)

def check_user_choice(input_length, input_choice):
  try:
    make_password(input_length, input_choice)
  except:
    error_p()

def make_password(plength, ctype):
  new_password = ""
  # check user choice
  if ctype == "2":
    new_password += random.choice(punctuation)
    user_choice_string = choices2
  else:
    new_password += random.choice(digits)
    user_choice_string = choices1
  # ensure at least one of every character type
  new_password += random.choice(lowercase)
  new_password += random.choice(uppercase)
  new_password += random.choice(digits)

  for i in range(int(plength)-4):
    letter = random.choice(user_choice_string)
    new_password += letter

  #https://stackoverflow.com/a/2668325
  l = list(new_password)
  random.shuffle(l)
  new_password = ''.join(l)

  print("The new password is: " + new_password)

start_p()