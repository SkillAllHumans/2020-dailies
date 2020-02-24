import sys

def start_p():
  print("Enter q to quit.")
# side 1
  a = input("Enter your first angle --> ")
  _check_if_quit(a.lower())
# side 2
  b = input("Enter your second angle --> ")
  _check_if_quit(b.lower())
# side 3
  c = input("Enter your third angle (optional) --> ")
  _check_if_quit(c.lower())
# next
  check_input(int(a), int(b), c)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q" or str(choice).lower() == "quit":
    print(msg)
    exit(0)

def check_input(a, b, c):
  if c == "":
    c = int(180 - (int(a) + int(b)))
    print(f"The missing angle is {c}.")
  if (a + b + c == 180) and (1 < a < 178) and (1 < b < 178) and (1 < c < 178):
    get_triangle_info(a, b, c)
  else:
    _check_if_quit("q", "Invalid input.")

def get_triangle_info(a, b, c):
  triangle_type = _get_triangle_type(a, b, c)
  angle_type = _get_angle_type(a, b, c)
  print(f"Angles {a}, {b}, {c} make the triangle type {angle_type} {triangle_type}.")

def _get_triangle_type(a, b, c):
  if a == b and b == c:
    return "equilateral"
  elif a == b or b == c or c == a:
    return "isosceles"
  else:
    return "scalene"

def _get_angle_type(a, b, c):
  if a > 90  or b > 90 or c > 90:
    return "obstuse"
  elif a == 90  or b == 90 or c == 90:
    return "right"
  else:
    return "acute"

# call on load
start_p()