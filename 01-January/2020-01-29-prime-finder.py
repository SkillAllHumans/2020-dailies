import sys
import datetime

def start_p():
  print("Enter q at any time to quit.")
  input_number = input("Enter how many primes (between 2 and 1000) you'd like to find. --> ")
  # test input right away
  check_if_quit(input_number.lower())
  input_to_int = int(input_number)
  if input_to_int > 1000 or input_to_int < 2:
    error_p("Enter number between 2 and 1000.")    
  # next
  get_primes_into_dictionary(input_to_int)

def error_p(text="Error. Try again."):
  print(text)
  exit(0)

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    exit(0)

def check_for_prime(number):
  if number < 2:
    return False
  elif number == 2:
    return True
  elif number % 2 == 0:
    return False
  else:
    temp_array = []
    for x in range(1, number+1):
      if number % x == 0:
        temp_array.append(x)
    if len(temp_array) == 2:
      return True

def get_primes_into_dictionary(input_number):
  primes = {}
  primes_array = []
  primes_desired = input_number
  start_number = 2

  while primes_desired > len(primes):
    y = check_for_prime(start_number)
    z = len(primes) + 1
    if y:
      primes[z] = start_number
      primes_array.append(str(start_number))
    start_number += 1
  # next
  output_results(primes, primes_array)

def output_results(primes, primes_array):
  print_string = ', '.join(primes_array)
  print(print_string)

  for key, val in primes.items():
    print(str(key) + ": " + str(val))

  save_to_file(primes, print_string)

def get_file_location():
  #Use this to save the file to the same directory as this program
  fname = "2020-01-29-prime-finder.py"
  fpath = __file__
  result = fpath.replace(fname, "")
  return result

def save_to_file(primes, print_string):
  yorn = input("Save this to file? (enter y) --> ")
  if yorn == "y" or yorn == "":
    filename = input("Name your file (include extension) --> ") or "prime-finder-" + datetime.datetime.now().strftime("%f") + ".txt"
    file = open(get_file_location() + filename, "a+") 
    file.write(print_string)
    file.write("\n")
    for key, val in primes.items():
      file.write(str(key) + ": " + str(val) + "\n")
    file.close()
    print("Your file is done!")
  else:
    check_if_quit("q")


# call on load
start_p()
