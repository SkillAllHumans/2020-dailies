import random
import sys
references = ["Cheers", "Friends", "Dexter", "The Simpsons", "Blackadder", "Law & Order", "Scrubs", "Star Trek",
  "Bewitched", "Mission: Impossible", "Seinfeld", "Bonanza", "Batman", "Dallas", "Twin Peaks", "Dragnet", "Dr. Who",
  "Wings", "Baywatch", "Remington Steele", "Dr. Quinn: Medicine Woman", "Oz", "The Wire", "The Price is Right",
  "M*A*S*H", "Murphy Brown", "The Fugitive", "a soap opera", "Sesame Street", "Jeopardy!",
  "a talent-search show", "a reality show", "The Today Show"]
locations = ["a regional airport", "a horse breeding farm", "a bakery", "a pharmacy", "a hospital", "an office",
  "a processing plant", "a restaurant", "a store", "a gym", "a military base", "a daycare center", "a school",
  "a house", "the past", "the future", "a prison", "a space colony", "a space ship", "Boston", "New York",
  "L.A.", "Washington", "the Midwest", "TV studio", "the West", "a war", "a rich neighborhood", "a poor community",
  "a small town", "a foreign land", "a fantasy kingdom", "a newsroom"]
withAs = ["sassy child", "member of a visible minority", "performing dog", "know-it-all secretary",
  "middle-aged woman who behaves lecherously for laughs", "crude grandparent tellin' it like it used to be",
  "bevy of weekly 'hey-I've-seen-them-somewhere-before' guests", "dark secret", "drug problem",
  "disabling fear of commitment", "year to live", "gambling debt", "rare set of skills", "nervous sidekick",
  "very intrusive neighbor", "retired cop", "trendy mental illness", "wisecracking teenager", "35-year-old teenager",
  "terrible attempt at an accent, based on accepted stereotypes", "dutiful manservant", "beleaguered single parent",
  "sunny outlook on global collapse", "bloody history of covert operations", "prog-rock theme song", "idiot savant",
  "wise person with a moderate disability", "hapless father", "sad story that explains all personal failings",
  "homely man married to a woman way out of his league with whom he has no chemistry", "vaguely 'ethnic' neighbor",
  "competition over a chintzy prize", "person who came here to make friends"]

def start_p():
  print("******Make a show premise like the big producers do! Enter 'q' at any time to quit.******")
  make_show()

def make_show():
  tempr = random.choice(references)
  templ = random.choice(locations)
  tempw = random.choice(withAs)
  show = "It's like " + tempr + " set in " + templ + " with a " + tempw + "."
  print(show)
  file_choice(show)

def check_if_quit(choice):
  if str(choice).lower() == "q":
    print("Goodbye!")
    exit(0)

def file_choice(show):
  choice = input("Enter 'y' or 'yes' to save this to a file. ")
  check_if_quit(choice)
  if str(choice).lower() == "y" or str(choice) == "yes":
    input_file_name = input("What should the file be called? (Letters and numbers; don't add a file extension) --> ")
    check_if_quit(input_file_name)
    make_file(show, input_file_name)
  else:
    make_show()

def get_file_location():
  fname = "2020-02-06-sitcom-dartboard.py"
  fpath = __file__
  result = fpath.replace(fname, "")
  return result

def make_file(show, input_file_name):
  # handle empty filename string
  if input_file_name == "":
    input_file_name = "sitcom-dartboard"
  filename = input_file_name + ".txt"
  f = open(get_file_location() + filename, "a+")
  f.write(str(show) + "\n")
  f.close()
  print("Your file is done!")
  make_show()

start_p()
