from Characters import Character

class Warrior (Character):

  def __init__(self, nombre, fuerza, inteligencia, defensa, vitality, espada):
    super().__init__(nombre, fuerza, inteligencia, defensa, vitality)
    self.espada = espada
    
  def atributos(self):
    super().atributos()
    print(f"Espada: {self.espada}")

  def cambiar_arma(self):
    opcion = 0
    while(opcion == 0):
      opcion = int(input("Elige un arma. (1) Espada de Hierro: daño 8. (2) Espada de Acero: daño 10."))
      if(opcion == 1):
        self.espada = 8
        break
      elif(opcion == 2):
        self.espada = 10
        break
      else:
        print("Número de arma incorrecto")
        opcion = 0
  
  def damage(self, enemigo):
    damage = self.fuerza + self.espada + (self.fuerza * self.espada) / 100
    return damage - enemigo.defensa