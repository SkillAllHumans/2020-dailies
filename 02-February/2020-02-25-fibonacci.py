import sys

def start_p():
  print("Enter q to quit.")
  input_number = input("Which Fibonacci number do you want? --> ")
  # test input right away
  _check_if_quit(input_number.lower())
  # next
  check_input(int(input_number))

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice) == "":
    print(msg)
    exit(0)

def check_input(input_number):
  if input_number > -1 and input_number < 100:
    if input_number == 0 or input_number == 1:
      result_num = input_number
    else:
      result_num = _fib_function(input_number)
    print(f"Number {input_number} in the Fibonnaci sequence is {result_num}.")
  else:
    _check_if_quit("q", "Invalid input.")

def _fib_function(input_number):
  result_nums = [0, 1]
  for x in range(2, input_number + 1):
    result_nums.append((result_nums[x - 1]) + (result_nums[x - 2]))
  return result_nums.pop()

# call on load
start_p()