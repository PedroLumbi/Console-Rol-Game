import os
from Game.Characters.Warrior import Warrior
from Game.Characters.Character import Character

mi_enemigo = Character("Goblin", 2, 1, 0, 50)

mi_personaje = Warrior("Pedro", 5, 1, 2, 100, 10)

def character_selection():
  print("Bienvenido!")

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
  mi_personaje.atributos()
  input()

def case2():
  clear()
  print("case 2")
  mi_personaje.atacar(mi_enemigo)
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

def run():
  
  main_menu()

def input_int(text):
  try:
    option = int(input(text))
  except ValueError:
    print("Por favor ingrese solo números que se muestran en las opciones")
    input()

  if type(option) is int:
    return option

def clear():
  os.system('clear')