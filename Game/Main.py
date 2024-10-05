import os
from Game.Characters.Character import Character
from Game.Characters.Warrior import Warrior
from Game.Characters.Archer import Archer
from Game.Characters.Wizard import Wizard

main_character = Character("")

def run():
  
  character_selection()

def character_selection():
  clear()
  print("Bienvenido!")
  print("(1) Gerrero")
  print("(2) Arquero")
  print("(3) Mago")
  rol = input_int("Eliga una de las opciones de clase para iniciar: ")

  name = input("Escribe el nombre del personaje: ")

  global main_character
  if rol == 1:
    main_character = Warrior(name, 5, 0, 2, 3, 5)
  elif rol == 2:
    main_character = Archer(name, 7, 0, 1, 2, 10)
  elif rol == 3:
    main_character = Wizard(name, 0, 8, 0, 2, 10)
  else:
    character_selection()

  main_menu()

def main_menu():
  while True:
    clear()
    print("********INICIO********")
    print("* (1) Ver atributos  *")
    print("* (2) Ir de aventura *")
    print("* (3) Inventario     *")
    print("* (4) Tienda         *")
    print("* (5) Descansar      *")
    print("*                    *")
    print("*                    *")
    print("* (0) Finalizar      *")
    print("**********************")

    options = {
      1: case1,
      2: case2,
      3: case3,
      4: case4,
      5: case5,
    }

    option  = input_int("Seleccione una opción --> ")
    if option == 0: break
    options.get(option, default_case)()

def case1():
  clear()
  main_character.atributos()
  input()

def case2():
  clear()
  enemigo = Character("Goblin", 2, 1, 0, 1)
  main_character.atacar(enemigo)
  input()

def case3():
  clear()
  print("case 3")
  input()

def case4():
  clear()
  print("case 4")
  input()

def case5():
  clear()
  print("case 5")
  input()

def default_case():
    print("Caso no reconocido")

def combat_menu():
  pass

def input_int(text):
  try:
    option = int(input(text))
  except ValueError:
    print("Por favor ingrese solo números que se muestran en las opciones")
    input()

  if type(option) is int:
    return option
  else:
    return 123

def clear():
  os.system('clear')