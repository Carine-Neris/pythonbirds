class Pessoa:
    """O atributo de class é acessado pela classe e pelos objetos"""
    olhos = 2

    """ Usamos o método especial __init__ para inicializar os atributos da classe """
    def __init__(self,*filhos:list,nome:str,idade:int):
        
        """ O parametro self é uma convenção no python, porém o método poderia
        receber qualquer palavra reservada, quando chamamos o método o python
        passa implicitamente o objeto por parametro """

        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
   
        
    def comprimentar(self) -> str: 
        return f'Olá {id(self)}' 

    @staticmethod
    def metodo_estatico():
        return f'Eu sou um método de classe'

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f' {cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass

if __name__ == '__main__':
    p = Homem(nome='Carine',idade=29)
    c = Pessoa(p,nome="Barbara",idade=28)
    print(p.comprimentar())
    print(Pessoa.comprimentar(p))
    print(id(p))

    print(c.olhos)
    print(p.olhos)

    for filhos in c.filhos:
        print(filhos.nome)

    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())


    #Metodo para saber se um objeto é instancia da classe
    print(isinstance(p,Pessoa))
    print(isinstance(c,Homem))