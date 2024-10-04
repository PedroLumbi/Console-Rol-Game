class Character:

  def __init__(self, nombre, fuerza = 0, inteligencia = 0, defensa = 0, vitality = 1):
    self.nombre = nombre
    self.level = 0
    self.experience = 0
    self.fuerza = fuerza
    self.inteligencia = inteligencia
    self.defensa = defensa
    self.vitality = vitality
    self.max_hp = vitality * 100
    self.hp = self.max_hp

  def information():
    return "Descripción de personaje"

  def atributos(self):
    print(f"-- {self.nombre} --")
    print(f"Level: {self.level}")
    print(f"Experience: {self.experience}")
    print(f"Fuerza: {self.fuerza}")
    print(f"Inteligencia: {self.inteligencia}")
    print(f"Defensa: {self.defensa}")
    print(f"Vitality: {self.vitality}")
    print(f"HP: {self.hp} / {self.max_hp}")

  def subir_nivel(self, fuerza, inteligencia, defensa, vitality):
    self.fuerza = self.fuerza + fuerza
    self.inteligencia = self.inteligencia + inteligencia
    self.defensa = self.defensa + defensa
    self.vitality = self.vitality + vitality

  def cambiar_arma(self):
    pass
  
  def esta_vivo(self):
    return self.hp > 0
  
  def morir(self):
    self.hp = 0
    print(f"{self.nombre} ha muerto")
  
  def damage(self, enemigo):
    return self.fuerza - enemigo.defensa
  
  def atacar(self, enemigo):
    damage = self.damage(enemigo)
    enemigo.hp = enemigo.hp - damage
    print(f"[{self.nombre}] Ha realizado {damage} puntos de daño a {enemigo.nombre}")
    if(enemigo.esta_vivo()):
      print(f"Los HP de {enemigo.nombre} son {enemigo.hp}")
    else:
      enemigo.morir()




