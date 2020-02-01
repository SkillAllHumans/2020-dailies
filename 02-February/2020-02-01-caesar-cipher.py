import sys
from functools import reduce

# globals
alphabet_string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
digits_and_punctuation = "0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def start_p():
  print("Enter q at any time to quit.")
  input_phrase = input("Enter your text to encrypt. (Note: not case-sensitive.) --> ")
  # test input right away
  check_if_quit(input_phrase.lower())

  input_offset = input("Enter your offset (1-25). --> ")
  check_if_quit(input_offset.lower())
  if int(input_offset) < 1 or int(input_offset) > 25:
    error_p("Offset must be from 1 to 25.")
  # next
  remove_excess_spaces(input_phrase.lower(), input_offset)

def error_p(text="Error. Try again."):
  print(text)
  exit(0)

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    exit(0)

def remove_excess_spaces(input_phrase, input_offset):
  # https://stackoverflow.com/a/21063580
  result = reduce(lambda x, y: x if x[-1]==' ' and y==' ' else x+y, input_phrase) if input_phrase else ''
  if "  " in result:
    remove_excess_spaces(result)
  else:
    check_user_choice(result, input_offset)

def check_user_choice(input_phrase, input_offset):
  if len(input_phrase) > 500:
    print("Your phrase has been shortened to 500 characters.")
  # next
  change_letters_by_offset(input_phrase[:500], input_offset)

def change_letters_by_offset(input_phrase, input_offset):
  result_string = ""

  for letter in input_phrase:
    if letter not in digits_and_punctuation:
      temp = int(alphabet_string.find(letter)) + int(input_offset)
      result_string += alphabet_string[temp]
    else:
      result_string += letter

  # next
  print(result_string)

# call on load
start_p()