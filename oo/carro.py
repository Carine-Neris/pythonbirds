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

NORTE = "Norte"
LESTE = "Leste"
SUL = "Sul"
OESTE = "Oeste"

class Direcao():
   def __init__(self):
      self.valor = "Norte"

   #Usando Dict
   def girar_a_direita(self):
      direcao_direita_dict = {
         "Norte":LESTE , "Leste":SUL, "Sul":OESTE, "Oeste":NORTE
      }

      self.valor = direcao_direita_dict[self.valor]
      return self.valor   

   #Usando estrutura de Decisão
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

   def calcular_velocidade(self):
      return self.motor.velocidade

   def acelerar(self):
      return self.motor.acelerar()

   def frear(self):
      return self.motor.frear()

   def calcular_direcao(self):
      return self.direcao.valor

   def girar_a_direita(self):
      return self.direcao.girar_a_direita()

   def girar_a_esquerda(self):
      return self.direcao.girar_a_esquerda()


if __name__ == "__main__":
   motor = Motor()
   direcao = Direcao()
   carro = Carro(direcao, motor)
   print(carro.calcular_velocidade())
   carro.acelerar()
   print(carro.calcular_velocidade())
   carro.girar_a_direita()
   print(carro.calcular_direcao())
   carro.girar_a_direita()
   print(carro.calcular_direcao())
   carro.girar_a_direita()
   print(carro.calcular_direcao())
   carro.girar_a_direita()
   print(carro.calcular_direcao())