from Game.Characters.Character import Character
from Game.Characters.Warrior import Warrior
from Game.Characters.Wizard import Wizard
from Game.Characters.Archer import Archer

def goblin():
  return Warrior("Goblin", 2, 1, 1, 1, 4)

def orco():
  return Warrior("Orco", 10, 1, 5, 3, 12)