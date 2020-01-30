import sys
from functools import reduce

def start_p():
  print("Enter q at any time to quit.")
  input_phrase = input("Enter your text to analyze. (Note: not case-sensitive.) --> ")
  # test input right away
  check_if_quit(input_phrase.lower())    
  # next
  remove_excess_spaces(input_phrase.lower())

def error_p(text="Error. Try again."):
  print(text)
  exit(0)

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    exit(0)

def remove_excess_spaces(input_phrase):
  # https://stackoverflow.com/a/21063580
  result = reduce(lambda x, y: x if x[-1]==' ' and y==' ' else x+y, input_phrase) if input_phrase else ''
  if "  " in result:
    remove_excess_spaces(result)
  else:
    check_user_choice(result)

def check_user_choice(input_phrase):
  if len(input_phrase) > 500:
    print("Your phrase has been shortened to 500 characters.")
  # next
  break_string_input_into_array(input_phrase[:500])

def break_string_input_into_array(input_phrase):
  phrase_array = input_phrase.split(" ")
  word_count = len(phrase_array)
  result_dict = {}

  for word in phrase_array:
    if word not in result_dict:
      result_dict[word] = 1
    else:
      result_dict[word] += 1
  # next
  sort_and_display_counts(input_phrase, word_count, result_dict)

def sort_and_display_counts(input_phrase, word_count, result_dict):
  print("Your input phrase was " + input_phrase)
  print("It has " + str(word_count) + " words.")
  for word in result_dict:
    temp = (result_dict[word]/word_count)
    # format from https://stackoverflow.com/a/5306787
    print(word + " occurs " + str(result_dict[word]) +
      " times in the phrase. This is " + "{0:.2%}".format(temp) +
      " percent of the phrase.")

# call on load
start_p()