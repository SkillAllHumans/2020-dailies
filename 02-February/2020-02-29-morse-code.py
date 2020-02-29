import sys

# globals
chars_dict = {
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "0": "-----"
}

def start_p():
  print("Enter q to quit.")
  input_string = input("Enter the string you to convert to morse code. --> ")
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
    analyze_string(input_string.lower())
  else:
    _check_if_quit("q", msg = "Check your string length.")

def analyze_string(input_string):
  new_str = _convert_chars(input_string)
  
  print(f"{input_string} is {new_str}\nin morse code (only numbers and letters translated).")

def _convert_chars(input_string):
  new_str = ""
  for x in input_string:
    if x in chars_dict:
      new_str += "\n\t" + chars_dict[x]
    else:
      new_str += " "

  return new_str 

# call on load
start_p()