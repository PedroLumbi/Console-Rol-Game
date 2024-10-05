from Game.Characters.Character import Character

class Wizard(Character):
  
  def __init__(self, nombre, fuerza=0, inteligencia=0, defensa=0, vitality=1):
    super().__init__(nombre, fuerza, inteligencia, defensa, vitality)

  def atributos(self):
    return super().atributos()
  
  def cambiar_arma(self):
    return super().cambiar_arma()
  
  def atacar(self, enemigo):
    return super().atacar(enemigo)