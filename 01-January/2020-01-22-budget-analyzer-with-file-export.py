import datetime

def start_budgeting():
  #Prompt user for initial input
  print("Welcome to the monthly budget analyzer!")
  budget_total = input("What was the total amount you've budgeted for the month? --> ")

  #Convert string to float
  budget_total = float(budget_total)

  #Set variables for use in the collection loop
  total_monthly_expenses = 0
  names_and_vals_monthly_expenses = {}
  continue_budgeting = True

  #Start the loop to collect monthly expenses
  while continue_budgeting == True:
    temp_name = input("Name of the budget item --> ")
    temp_cost = input("Cost of the budget item --> ")

    #Check that the budget item name is unique
    if temp_name in names_and_vals_monthly_expenses:
      temp_name = temp_name + "1"

    #Push k, v pair to dictionary
    names_and_vals_monthly_expenses[temp_name] = temp_cost
    #Show that the input was accepted
    print("You added $" + temp_cost + " to cover the cost of " + temp_name + ".")

    #Convert string to float
    temp_cost = float(temp_cost)
    #Add cost to monthly total
    total_monthly_expenses += temp_cost

    #Break if done
    response = input("Do you wish to add more? --> ")
    #Decide whether to continue based on user input
    response = response.lower()
    if response == "n" or response == "no":
      print ("Okay.")
      continue_budgeting = False

  #Print out results
  print_out_results(budget_total, names_and_vals_monthly_expenses, total_monthly_expenses)

def print_out_results(budget_total, names_and_vals_monthly_expenses, total_monthly_expenses):
  #Print overview
  line1 = "Your total monthly budget is $" + "{0:.2f}".format(budget_total) + " and your total monthly expenses are $" + "{0:.2f}".format(total_monthly_expenses) + " for " + str(len(names_and_vals_monthly_expenses)) + " expenses."
  print(line1)
  #Change answer depending on pos/neg outcome
  over_under = budget_total - total_monthly_expenses
  if over_under >= 0:
    line2 = "This leaves you with $" + "{0:.2f}".format(over_under) + " after expenses. You made it!"
  else: 
    line2 = "This leaves you with a deficit of $" + "{0:.2f}".format(over_under) + " and will not cover your expenses."
  print(line2)

  #Print each item and cost (https://stackoverflow.com/a/26660785)
  line3 = "Your itemized expenses are: "
  print(line3)
  line_array = []
  for k, v in names_and_vals_monthly_expenses.items():
    line_array.append("\t---------------------------------------------------------")
    print("\t---------------------------------------------------------")
    line_array.append("\tExpense name: " + k + "\n\tExpense cost: " + v)
    print("\tExpense name: " + k + "\n\tExpense cost: " + v)
    #Send to .txt file
  save_to_file(line1, line2, line3, line_array)

def get_file_location():
  #Use this to save the file to the same directory as this program
  fname = "2020-01-23-budget-analyzer-with-file-export.py"
  fpath = __file__
  result = fpath.replace(fname, "")
  return result

def save_to_file(line1, line2, line3, larray):
  filename = "your-budget-" + datetime.datetime.now().strftime("%f") + ".txt"
  file = open(get_file_location() + filename, "a+") 
  file.write(line1+"\n")
  file.write(line2+"\n")
  file.write(line3+"\n")
  for line in larray:
    file.write(str(line) + "\n")
  file.close()
  print("Your file is done!")

#Call the function
start_budgeting()