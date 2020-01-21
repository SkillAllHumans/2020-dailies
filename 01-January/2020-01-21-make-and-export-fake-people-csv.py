# https://stackoverflow.com/a/1058727
import random
import sys
names = ["Mohamed",
  "Youssef",
  "Ahmed",
  "Mahmoud",
  "Mustafa",
  "Yassin",
  "Taha",
  "Khaled",
  "Hamza",
  "Bilal",
  "Ibrahim",
  "Hassan",
  "Hussein",
  "Karim",
  "Tareq",
  "Abdel",
  "Rahman",
  "Ali",
  "Omar",
  "Halim",
  "Halima",
  "Murad",
  "Selim",
  "Abdallah",
  "Shaimaa",
  "Fatma",
  "Fatima",
  "Maha",
  "Reem",
  "Farida",
  "Aya",
  "Shahd",
  "Ashraqat",
  "Sahar",
  "Fatin",
  "Dalal",
  "Doha",
  "Fajr",
  "Suha",
  "Rowan",
  "Hosniya",
  "Hasnaa",
  "Hosna",
  "Gamila",
  "Gamalat",
  "Habiba",
  "Santiago",
  "Mateo",
  "Juan",
  "Matias",
  "Nicolas",
  "Benjamin",
  "Pedro",
  "Tomas",
  "Thiago",
  "Santino",
  "Luis",
  "Jose",
  "Alexander",
  "David",
  "Angel",
  "Carlos",
  "Sebastian",
  "Daniel",
  "Jesus",
  "Sofia",
  "Maria",
  "Lucia",
  "Martina",
  "Catalina",
  "Elena",
  "Emilia",
  "Valentina",
  "Paula",
  "Zoe",
  "Mariana",
  "Isabella",
  "Valeria",
  "Gabriela",
  "Sara",
  "Salome",
  "Daniela",
  "Victoria",
  "Mia",
  "Amanda",
  "Mikaela",
  "Camila",
  "Amaia",
  "Emma",
  "Kamila",
  "Sofia",
  "Wei",
  "Jie",
  "Hao",
  "Yi",
  "Jun",
  "Feng",
  "Yong",
  "Jian",
  "George",
  "Elias",
  "Majd",
  "Yusuf",
  "Hana",
  "Julian",
  "Charbel",
  "Adam",
  "Omri",
  "Eyal",
  "Amir",
  "Salman",
  "Rani",
  "Tamir",
  "Yosef",
  "Noam",
  "Amit",
  "Ariel",
  "Adi",
  "Yuval",
  "Yahli",
  "Omer",
  "Lior",
  "Maria",
  "Celine",
  "Aline",
  "Maya",
  "Noor",
  "Lian",
  "Maryam",
  "Natalie",
  "Tala",
  "Miral",
  "Eden",
  "Yarin",
  "Nur",
  "Sarah",
  "Sillin",
  "Assil",
  "Malk",
  "Miyar",
  "Sakura",
  "Riko",
  "Aoi",
  "Wakana",
  "Rin",
  "Anna",
  "Azuna",
  "Himari",
  "Hinata",
  "Yuna",
  "Yuina",
  "Kaede",
  "Lukas",
  "Maximilian",
  "Jakob",
  "Tobias",
  "Paul",
  "Jonas",
  "Jakub",
  "Jan",
  "Tomas",
  "Matyas",
  "Filip",
  "Vojtech",
  "Ondrej",
  "Lukas",
  "Noah",
  "Victor",
  "Oliver",
  "Oscar",
  "William",
  "Lucas",
  "Carl",
  "Emil",
  "Malthe",
  "Frederik",
  "Magnus",
  "Harry",
  "Jack",
  "Jacob",
  "Charlie",
  "Muhammad",
  "Thomas",
  "Rasmus",
  "Robin",
  "Maksim",
  "Robert",
  "Martin",
  "Kaspar",
  "Andrei",
  "Alexandru",
  "Gabriel",
  "Mihai",
  "Cristian",
  "Stefan",
  "Eliska",
  "Tereza",
  "Adela",
  "Natalie",
  "Sofie",
  "Kristyna",
  "Karolina",
  "Viktorie",
  "Freja",
  "Alma",
  "Laura",
  "Ida",
  "Clara",
  "Ella",
  "Josefine",
  "Olivia",
  "Amelia",
  "Emily",
  "Isla",
  "Ava",
  "Jessica",
  "Lily",
  "Elise",
  "Sandra",
  "Alisa",
  "Grace",
  "Sophie",
  "Aoife",
  "Lucy",
  "Nora",
  "Maja",
  "Ingrid",
  "Emilie",
  "Zuzanna",
  "Julia",
  "Lena",
  "Hanna",
  "Zofia",
  "Alicja",
  "Aleksandra",
  "Natalia",
  "Leonor",
  "Leonord",
  "Leonora",
  "Leonore",
  "Matilde",
  "Beatriz",
  "Carolina",
  "Ana",
  "Ines",
  "Margarida",
  "Ioana",
  "Andreea",
  "Alexandra",
  "Antonia",
  "Daria"];



def start_p():
  print("Enter a single q to quit program.")
  input_amount = input("How many people (between 1-1000) do you want to make? --> ")
  check_if_quit(input_amount)
  input_file_name = input("What should the file be called? (Letters and numbers ONLY) --> ")
  check_if_quit(input_file_name)

  check_user_choice(input_amount, input_file_name)

    
def quit_p():
  exit(0)

def error_p(text="Error. Try again."):
  print(text)
  start_p()

def check_if_quit(choice):
  if str(choice).lower() == "q" or str(choice) == "":
    print("Goodbye!")
    quit_p()

def check_user_choice(input_amount, input_file_name):
  try:
    val = int(input_amount)
    if val < 1 or val > 1000:
      error_p("Enter a number from 1 to 1000")
    make_people(val, input_file_name)
  except:
    error_p()

def make_people(input_amount, input_file_name):
  people = []
  for i in range(input_amount):
    tempf = random.choice(names)
    templ = random.choice(names)
    temp = tempf + "," + templ
    people.append(temp)
  make_file(input_amount, input_file_name, people)

def get_file_location():
  fname = "2020-01-21-make-and-export-fake-people-csv.py"
  fpath = __file__
  result = fpath.replace(fname, "")
  return result

def make_file(input_amount, input_file_name, people):
  filename = input_file_name + ".txt"
  f = open(get_file_location() + filename, "a+")

  for person in people:
    print(str(person))
    f.write(str(person) + "\n")
  f.close()
  print("Your file is done!")

start_p()
