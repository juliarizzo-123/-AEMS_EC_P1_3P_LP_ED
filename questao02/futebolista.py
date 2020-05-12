from atleta import Atleta

class Futebolista(Atleta):
    def __init__(self,nome, idade,gols):
        self.gols = gols
        super().__init__(nome, idade)
   
    def faz_o_que(self, nome,gols):

        self.futebolista =("O" +nome+ "é jogador de futebol e já marcou: " +gols+ " gols!! \n")
        return self.futebolista
        