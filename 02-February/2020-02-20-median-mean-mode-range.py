import sys
from collections import Counter

def start_p():
  print("Enter q to quit.")
  input_list = input("Enter the integers that you want to examine, separated by a comma. --> ")
  # test input right away
  _check_if_quit(input_list.lower())
  # next
  check_input(_strip_chars(input_list," ", ""))

def _strip_chars(input_list, findc, replacec):
  return input_list.replace(findc, replacec)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_list):
  # are all chars digits?
  if type(int(_strip_chars(input_list,",", ""))) == int:
    # make string into array, then sort
    new_list = input_list.split(",")
    new_list.sort()
    # get values for output
    mean = get_mean(new_list)
    median = get_median(new_list)
    mode = get_mode(new_list)
    numrange = get_range(new_list)
    # output
    print(f" The mean of {input_list} is {mean}.\n The median is {median}.\n {mode}\n The range is {numrange}.")
  else:
    _check_if_quit("q", "Invalid input.")

def get_mean(new_list):
  total = 0
  for x in new_list:
    total += int(x)
  return total/len(new_list)

def get_median(new_list):
  list_length = len(new_list)
  if list_length % 2 == 0:
    # get, average middle vals
    half_length = list_length/2
    median = (int(new_list[int(half_length)])+int(new_list[int(half_length-1)]))/2
  else:
    median = new_list[int((list_length+1)/2)]
  return median

def get_mode(new_list):
  # https://stackoverflow.com/a/5829377
  new_dict = Counter(new_list) # Took out the following; this doesn't account for all values occurring the same number of times: m = max(new_dict)

  # from https://stackoverflow.com/a/613218
  sorted_by_value = sorted(new_dict.items(), key=lambda kv: kv[1])
  if sorted_by_value[-1][1] == sorted_by_value[-2][1]:
    return "There is no mode for this series."
  else:
    return "The mode is " + str(sorted_by_value[-1][0]) + ", which occurs " + str(sorted_by_value[-1][1]) + " times in the sequence."

def get_range(new_list):
  return int(new_list[-1]) - int(new_list[0])
  
# call on load
start_p()
