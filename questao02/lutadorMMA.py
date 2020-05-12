from atleta import Atleta
class LutadorMMA(Atleta):
    def __init__(self,nome, idade,categoria_de_peso,cinturoes_disputados):
        self.categoria_de_peso = categoria_de_peso
        self.cinturoes_disputados = cinturoes_disputados
        super().__init__(nome, idade)
   
    def faz_o_que(self,nome,categoria_de_peso,cinturoes_disputados):

        self.lutador =('O' +nome+'é um lutador de MMA na categoria : '+str(categoria_de_peso)+ ' kg e já disputou: '+str(cinturoes_disputados)+ ' cinturões !!\n')
        return self.lutador