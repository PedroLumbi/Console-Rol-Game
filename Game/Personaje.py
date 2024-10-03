class Personaje:

  def __init__(self, nombre, fuerza = 0, inteligencia = 0, defensa = 0, vida = 0):
    self.nombre = nombre
    self.fuerza = fuerza
    self.inteligencia = inteligencia
    self.defensa = defensa
    self.vida = vida

  def atributos(self):
    print(f"-- {self.nombre} --")
    print(f"Fuerza: {self.fuerza}")
    print(f"Inteligencia: {self.inteligencia}")
    print(f"Defensa: {self.defensa}")
    print(f"Vida: {self.vida}")

  def subir_nivel(self, fuerza, inteligencia, defensa, vida):
    self.fuerza = self.fuerza + fuerza
    self.inteligencia = self.inteligencia + inteligencia
    self.defensa = self.defensa + defensa
    self.vida = self.vida + vida
  
  def esta_vivo(self):
    return self.vida > 0
  
  def morir(self):
    self.vida = 0
    print(f"{self.nombre} ha muerto")
  
  def daño(self, enemigo):
    return self.fuerza - enemigo.defensa
  
  def atacar(self, enemigo):
    daño = self.daño(enemigo)
    enemigo.vida = enemigo.vida - daño
    print(f"[{self.nombre}] Ha realizado {daño} puntos de daño a {enemigo.nombre}")
    if(enemigo.esta_vivo()):
      print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
    else:
      enemigo.morir()

class Guerrero (Personaje):
  def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
    super().__init__(nombre, fuerza, inteligencia, defensa, vida)
    self.espada = espada

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
    
  def atributos(self):
    super().atributos()
    print(f"Espada: {self.espada}")
  
  def daño(self, enemigo):
    return self.fuerza * self.espada - enemigo.defensa


