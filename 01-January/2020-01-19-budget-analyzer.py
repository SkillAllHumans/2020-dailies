# Write a program that asks the user to enter the amount that he or she has budgeted for a month. A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total. When the loop finishes, the program should display the amount that the user is over or under budget.

# In each repetition through the loop, the program should prompt the user for name of the expense and the amount of the expense. The program should print the name of the expense and the amount of the expense. keep a running total of all expenses entered. When the loop finishes, the program should display the total amount that the user entered and indicate if the total amount is over or under budget.


# The program should print the amount of the expense for each item next to item name
# The program should display the amount budgeted
# The program should display the amount actually spent
# The program should display the amount that the user is over or under budge
# indicate if the total amount is over or under budget.


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
  print("Your total monthly budget is $" + "{0:.2f}".format(budget_total) + " and your total monthly expenses are $" + "{0:.2f}".format(total_monthly_expenses) + " for " + str(len(names_and_vals_monthly_expenses)) + " expenses.")
  #Change answer depending on pos/neg outcome
  over_under = budget_total - total_monthly_expenses
  if over_under >= 0:
    print("This leaves you with $" + "{0:.2f}".format(over_under) + " after expenses. You made it!")
  else: 
    print("This leaves you with a deficit of $" + "{0:.2f}".format(over_under) + " and will not cover your expenses.")
  #Print each item and cost (https://stackoverflow.com/a/26660785)
  print("Your itemized expenses are: ")
  for k, v in names_and_vals_monthly_expenses.items():
    print("\t---------------------------------------------------------")
    print("\tExpense name: " + k + "\n\tExpense cost: " + v)

#Call the function
start_budgeting()
