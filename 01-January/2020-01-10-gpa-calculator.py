# If the student has a GPA  greater than or equal to 3.2 and less than 3.6, the program should display that the student is a cum laude student.

# If the student has a GPA greater than or equal to 3.6 and less than 3.8, the program should display that the student is a magna cum laude 3.6 student.

# If the student has a GPA greater than or equal to 3.8 and less than or equal to 4.0, the program should display that the student is a summa cum laude student.

# If the student has a GPA is below 2.0, the program should display that the student cannot graduate.

# If the student has a GPA between 2.0 and less than  3.2, the program should display that the student is eligible to graduate.
    
def start_over(phrase="Your input is not valid, try again."):
  print(phrase)
  start_gpa_sorter()
    
def quit_sorter():
  import sys
  exit(0)

def start_gpa_sorter():
  #Get student data from user
  print("Find out a student's standing based on GPA. Program will restart on invalid input. Type q to quit.")
  input_name = input("What is the student's name? -->")
  if input_name == "q":
    quit_sorter()
  input_gpa = input("What is the student's GPA? -->")
  if input_gpa == "q":
    quit_sorter()

  #Convert gpa input to float, test
  try: 
    input_gpa = float(input_gpa)
  except:
    start_over()
  sort_by_gpa(input_name, input_gpa)

def sort_by_gpa(input_name, input_gpa):
  #Find the student's gpa category, act on it
  if input_gpa >= 3.8 and input_gpa <= 4.0:
    gpa_news_print(input_name, str(input_gpa), "can", "summa cum laude")
  elif input_gpa >= 3.6 and input_gpa < 3.8:
    gpa_news_print(input_name, str(input_gpa), "can", "magna cum laude")
  elif input_gpa >= 3.2 and input_gpa < 3.6:
    gpa_news_print(input_name, str(input_gpa), "can", "cum laude")
  elif input_gpa < 3.2 and input_gpa >= 2.0:
    gpa_news_print(input_name, str(input_gpa), "can")
  elif input_gpa > 0 and input_gpa <= 2.0:
    gpa_news_print(input_name, str(input_gpa), "cannot")
  else:
    start_over()

#Deliver the news
def gpa_news_print(name, gpa, can_or_cannot, honors=False):
  output_sentence = name + " " + can_or_cannot + " graduate with their GPA of " + gpa
  if honors != False:
    output_sentence += " and " + honors + ", too! Congrats!"
  else:
    output_sentence += "."

  print(output_sentence)
  # start over
  start_over("Thanks! Try another student's data.")

#Call
start_gpa_sorter()