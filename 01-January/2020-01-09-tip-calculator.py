#Variables
percentages = [0.15, 0.18, 0.20, 0.25, 0.30, 0.35]
tips = []
meal_total = []
meal_cost = 0.00

#Create tax, tip function
def start_calculate_tax_tip():
  #reset https://stackoverflow.com/a/1400622
  tips[:] = []
  meal_total[:] = []
  meal_cost = 0.00
  #Prompt user for input
  print("Welcome to the tax and tip calculator!")
  meal_cost = input("What is the total cost of your meal minus tax? --> ")
  check_input(meal_cost)

#check input
def check_input(meal_cost):
  try:
    #Convert string to float
    meal_cost = float(meal_cost)
    complete_calculation(meal_cost)
  except:
    #https://stackoverflow.com/a/13022426
    import sys
    sys.exit(0)

def complete_calculation(meal_cost):
  #run functions
  calculate_tip_from_percent(meal_cost)
  calculate_total(meal_cost)
  format_output_strings()
  start_calculate_tax_tip()

#Get tip amounts
def calculate_tip_from_percent(meal_cost):
  for x in percentages:
    tips.append(x * meal_cost)

#Get meal totals
def calculate_total(meal_cost):
  for x in tips:
    meal_total.append(x + meal_cost)

def format_output_strings():
  #Print out results
  #Limit float values to 2 decimal spaces, convert to strings (https://docs.python.org/3/library/string.html#format-specification-mini-language)
  #https://docs.python.org/3.7/library/functions.html#zip
  #https://w3resource.com/python-exercises/string/python-data-type-string-exercise-36.php
  for x, y, z in zip(percentages, tips, meal_total):
    print("\t" + "{:.0%}".format(x) + " on your check is $" + "{0:.2f}".format(y) + " for a pre-tax total of $" + "{0:.2f}".format(z) + ".")

#Call the function
start_calculate_tax_tip()