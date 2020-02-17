import sys
import random

#Globals
quotes = [
  "To be, or not to be: that is the &&proper&&:\nWhether ’tis &&adverb&& in the mind to suffer\nThe slings and arrows of &&adjective&& fortune,\nOr to take arms against a &&noun&& of troubles,\nAnd by opposing &&verb&& them?",
  "This day is called the feast of &&proper&&:\nHe that outlives this &&noun&&, and comes &&adverb&& home,\nWill stand &&adjective&& when the day is named,\nAnd &&verb&& him at the name of Crispian.",
  "It is a truth &&adverb&& acknowledged, that a single &&proper&& in possession of a &&adjective&& fortune must be in want of a &&noun&&.",
  "It is a far, far &&adjective&& thing that I &&verb&&, than I have ever done; it is a &&adverb&&, &&adverb&& better &&noun&& that I go to than I have ever known."
]

def start_p():
  print("Enter q to quit.")
  input_noun = input("Enter a singular noun (book, princess, etc.) --> ")
  # test input right away
  _check_if_quit(input_noun.lower())
  input_proper_noun = input("Enter a proper noun (The Book of the Death, Leia, etc.)  --> ")
  # test input right away
  _check_if_quit(input_proper_noun.lower())
  input_verb = input("Enter a present-tense verb (drink, go, etc.) --> ")
  # test input right away
  _check_if_quit(input_verb.lower())
  input_adjective = input("Enter an adjective (tall, green, shapely, etc.) --> ")
  # test input right away
  _check_if_quit(input_adjective.lower())
  input_adverb = input("Enter an adverb (slowly, suddenly, etc.) --> ")
  # test input right away
  _check_if_quit(input_adverb.lower())
  #next
  replace_words_in_quotes(input_noun, input_proper_noun, input_verb, input_adjective, input_adverb)

def _check_if_quit(choice, msg = "Goodbye!"):
  if str(choice).lower() == "q":
    print(msg)
    exit(0)

def replace_words_in_quotes(input_noun, input_proper_noun, input_verb, input_adjective, input_adverb):
  quote = random.choice(quotes)

  # check is string is empty, give default value if so
  if (len(input_noun) < 1):
    input_noun = "shoe"
  if (len(input_proper_noun) < 1):
    input_proper_noun = "Gertrude"
  if (len(input_verb) < 1):
    input_verb = "smell"
  if (len(input_adjective) < 1):
    input_adjective = "toothy"
  if (len(input_adverb) < 1):
    input_adverb = "greedily"

  quote_print = quote.replace("&&noun&&", input_noun).replace("&&proper&&", input_proper_noun).replace("&&verb&&", input_verb).replace("&&adjective&&", input_adjective).replace("&&adverb&&", input_adverb)

  print(quote_print)

# call on load
start_p()