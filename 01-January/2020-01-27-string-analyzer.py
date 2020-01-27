import sys

# globals
vowels = "aeiou"

def start_p():
  print("Enter q to quit.")
  input_string = input("Enter the string you want analyzed. --> ")
  # test input right away
  _check_if_quit(input_string.lower())
  # next
  check_input(input_string)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_string):
  if len(input_string) > 1 and len(input_string) < 500:
    analyze_string(input_string)
  else:
    _check_if_quit("q", msg = "Check your string length.")

def analyze_string(input_string):
  input_array = input_string.split()
  print("*" * 80)
  print(f"Your input string is {len(input_string)} characters long, with {len(input_array)} words.")
  for x in input_array:
    vowels, consonants = _get_vowels(x)
    print(f"\t{x} is {len(x)} characters long, with {vowels} vowels and {consonants} consonants.")
  print("*" * 80)

def _get_vowels(x):
  vowel_count = 0
  for y in x:
    if y in vowels:
      vowel_count += 1
  consonant_count = len(x) - vowel_count
  return vowel_count, consonant_count

# call on load
start_p()
