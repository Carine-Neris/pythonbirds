class Motor():
   def __init__(self):
      self.velocidade = 0
   
   def acelerar(self):
      self.velocidade += 1
      return self.velocidade
   
   def frear(self):
      self.velocidade -= 2
      self.velocidade = max(0,self.velocidade)
      return self.velocidade


class Direcao():
   def __init__(self):
      self.valor = "Norte"

   def girar_a_direita(self):
      if self.valor == "Norte":
         self.valor = "Leste"
      elif self.valor == "Leste":
         self.valor = "Sul"
      elif self.valor == "Sul":
         self.valor = "Oeste"
      else:
         self.valor = "Norte"
      return self.valor   

   def girar_a_esquerda(self):
      if self.valor == "Norte":
         self.valor = "Oeste"
      elif self.valor == "Oeste":
         self.valor = "Sul"
      elif self.valor == "Sul":
         self.valor = "Leste"
      elif self.valor == "Leste":
         self.valor = "Norte"
      else:
         self.valor = "Oeste"
      return self.valor


class Carro():
   def __init__(self,direcao,motor):
      self.direcao = direcao
      self.motor = motor

   def calcular_velocidade(self, motor):
      return motor.velocidade


if __name__ == "__main__":
   motor = Motor()
   direcao = Direcao()
   carro = Carro(direcao, motor)
   print(carro.calcular_velocidade(motor))
   carro.acelerar()
   print(carro.calcular_velocidade(motor))