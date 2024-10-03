import random

def Welcome():
  print("Welcome to the Passwod Generator")
  print()

def Input_Phrase():
  return input("Write a phrase or sentence that is easy for you to remember.")
  # return "Mañana si me baño".lower()

def Transform_Phrase():
  text_list = list(Input_Phrase())

  return text_list

def Random_Chart(chart):
  return random.choice(dictionary.get(chart, [chart]))

def Create_Password():
  text_list = Transform_Phrase()
  for i in range(len(text_list)):
    text_list[i] = Random_Chart(text_list[i])

  return "".join(text_list)

def Run():
  Welcome()
  new_password = Create_Password()
  print(new_password)

dictionary = {
    " ": ["_", "-", "#"],
    "a": ["a", "A", "@", "4"],
    "b": ["b", "B", "8"],
    "c": ["c", "C", "(", "<"],
    "d": ["d", "D"],
    "e": ["e", "E", "3"],
    "f": ["f", "F"],
    "g": ["g", "G", "9", "6"],
    "h": ["h", "H"],
    "i": ["i", "I", "|", "1"],
    "j": ["j", "J", "¿"],
    "k": ["k", "K"],
    "l": ["l", "L", "|", "1"],
    "m": ["m", "M"],
    "n": ["n", "N"],
    "o": ["o", "O", "0"],
    "p": ["p", "P", "9"],
    "q": ["q", "Q", "9"],
    "r": ["r", "R"],
    "s": ["s", "S", "$", "5"],
    "t": ["t", "T", "+", "7"],
    "u": ["u", "U"],
    "v": ["v", "V"],
    "w": ["w", "W"],
    "x": ["x", "X", "*"],
    "y": ["y", "Y", "&"],
    "z": ["z", "Z", "2"]
}