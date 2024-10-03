import os
from Game import Personaje

def clear():
    os.system('clear')

def crear_personaje():
  print("Bienvenido!")
  print("Distribuye tu puntos de atributos")
  print("Tienes 10 puntos iniciales")


def inicio():
  pass

def en_combate():
  pass

def run():
  clear()
  
  mi_personaje = Personaje.Personaje("Pedro", 1, 1, 1, 100)

  # crear_personaje()

  # mi_enemigo = Personaje("Goblin", 2, 1, 2, 50)

  mi_personaje.atributos()