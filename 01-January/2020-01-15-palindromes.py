# set python version, https://stackoverflow.com/a/41901923
import sys
if sys.version_info[0] < 3:
  raise Exception("Python 3.6 or a more recent version is required.")

def start_p():
  input_p = input("Enter what you'd like to turn into a palindrome --> ")
  try:
    palindrome(input_p)
  except:
    quit_p()
    
def quit_p():
  exit(0)

def palindrome(phrase="racecar"): 
  r_phrase = phrase[::-1] # https://www.w3schools.com/python/python_howto_reverse_string.asp
  perfect_palindrome = phrase + r_phrase
  imperfect_palindrome = phrase + r_phrase[1:] # https://stackoverflow.com/a/663175
  output_print(phrase, r_phrase, perfect_palindrome, imperfect_palindrome)

#give user results
def output_print(phrase, r_phrase, perfect_palindrome, imperfect_palindrome):
  # https://www.programiz.com/python-programming/string-interpolation
  print(f"Your phrase {phrase} is {r_phrase} when backwards.")
  print(f"The perfect palindrome version is {perfect_palindrome}.")
  print(f"The imperfect palindrome version is {imperfect_palindrome}.")
  # start over
  restart_or_quit()

def restart_or_quit():
  yorn = input("This program will restart on enter. If you'd like to exit, type one of these: q, e, c, quit, exit, close. --> ")
  if yorn in {"q", "e", "c", "quit", "exit", "close"}: #https://docs.python.org/3/tutorial/datastructures.html#sets
    quit_p()
  else:
    start_p()

#Call
start_p()