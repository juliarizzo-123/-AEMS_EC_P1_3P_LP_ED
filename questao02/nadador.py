from atleta import Atleta
class Nadador(Atleta):
    def __init__(self,nome, idade,numero_de_medalhas,numero_olimpiadas_disputadas):
        self.numero_de_medalhas = numero_de_medalhas
        self.numero_olimpiadas_disputadas = numero_olimpiadas_disputadas
        super().__init__(nome, idade)
   
    def faz_o_que(self, nome, numero_de_medalhas, numero_olimpiadas_disputadas):

        self.nadador =("O" +nome+ " é um competidor de natação e já ganhou: " +str(numero_de_medalhas)+ " medalhas em:  "+str(numero_olimpiadas_disputadas)+  " olimpíadas!! \n")
        return self.nadador

        