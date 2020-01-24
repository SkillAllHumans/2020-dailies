def start():
  num = input("Enter your number ->")
  check_if_quit(num)
  check_user_choice(num)

def quit_p():
  exit(0)

def error_p(text="Error. Try again."):
  print(text)
  start()

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    quit_p()

def check_user_choice(num):
  try:
    num = int(num)
    if num < 15 or num > 1000:
      error_p("Number must be between 15 and 1000")
    else:
      fizz_buzz(num)
  except:
    error_p()


def fizz_buzz(num):
  for x in range(1, int(num)+1):
    if (x%15==0):
      print(str(x)+" is FizzBuzz") 
    elif (x%5==0):
      print(str(x)+" is Fizz")
    elif (x%3==0):
      print(str(x)+" is Buzz")
    else:
      print(str(x)+" is ----")
  
start()