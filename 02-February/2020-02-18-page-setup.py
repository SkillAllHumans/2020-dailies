import sys
import random

#Globals
output_string = '<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8">\n    <title>&&titletext&&</title>\n  </head>\n  <body>\n    <h1>&&h1text&&</h1>\n    <h2>&&h2text&&</h2>\n  </body>\n</html>'


def start_p():
  print("This program will generate an HTML page outline. Copy and paste the output into a text editor.")
  print("Enter q to quit. You can leave options blank.")
  input_title = input("Enter the title for your page --> ")
  # test input right away
  _check_if_quit(input_title.lower())
  input_h1 = input("Enter the first heading --> ")
  # test input right away
  _check_if_quit(input_h1.lower())
  input_h2 = input("Enter the sub-heading --> ")
  # test input right away
  _check_if_quit(input_h2.lower())
  #next
  replace_words_in_output_string(input_title, input_h1, input_h2)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q":
    print(msg)
    exit(0)

def replace_words_in_output_string(input_title, input_h1, input_h2):
  output = output_string.replace("&&titletext&&", input_title).replace("&&h1text&&", input_h1).replace("&&h2text&&", input_h2)
  print(output)
  file_choice(output)

def file_choice(output):
  choice = input("Enter 'y' or 'yes' to save this to a file. --> ")
  check_if_save(choice, output)

def check_if_save(choice, output):
  if str(choice).lower() == "y" or str(choice) == "yes":
    input_file_name = input("What should the file be called? (Letters and numbers; don't add a file extension)\n******NOTE: if a file by this name exists, this code will be appended to the end of the file. --> ")
    _check_if_quit(input_file_name)
    make_file(output, input_file_name)
  else:
    _check_if_quit("q", "Goodbye!")

def _get_file_location():
  fname = "2020-02-18-page-setup.py"
  fpath = __file__
  result = fpath.replace(fname, "")
  return result

def make_file(output, input_file_name):
  # handle empty filename string
  if input_file_name == "":
    input_file_name = "index"
  filename = input_file_name + ".html"
  f = open(_get_file_location() + filename, "a")
  f.write(output)
  f.close()
  print("Your file is done!")

# call on load
start_p()