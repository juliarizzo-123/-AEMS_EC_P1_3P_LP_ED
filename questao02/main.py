from futebolista import Futebolista
from atleta import Atleta
from nadador import Nadador
from lutadorMMA import LutadorMMA
op = 88
ec = 88
mostrar = 88
most = 88
fi=0
ni=0
mi=0


while op != 0:
    print("~"*30)
    print (' O que deseja fazer: \n 1 - Cadastrar atleta \n 2 - Mostrar Informação de atleta \n 0 - Sair do programa ')
    op = int(input('Qual é sua opção: '))
    
    if op == 1 :
        while ec != 0:
            print("[1] - Cadastrar Futebolista\n[2] - Cadastrar Nadador\n[3] - Cadastrar Lutador de MMA\n[0] - Retornar ao menu anterior")   
            ec = int(input('Qual sua opçao: '))
            if ec == 1:

                if fi < 1 :
                    print("~"*30)
                    print('Cadastrar Futebolista: ')
                    nome = input('Digite o nome: ') 
                    idade = int(input('Digite sua idade: '))
                    gols = input('Quantos gols marcou: ')
                    b = Futebolista(nome,idade ,gols)
                    fi = fi+1

                else:
                    print(" Maximos de atletas cadastrados")


            elif ec == 2 :
                if ni < 1:
                    print("~"*30)
                    print('Cadastrar Nadador: ')
                    nome = input('Digite o nome: ') 
                    idade = int(input('Digite sua idade: '))
                    numero_de_medalhas = int(input('numero de medalhas: '))
                    numero_olimpiadas_disputadas = int(input('numero olimpiadas disputadas: '))
                    P = Nadador(nome, idade,numero_de_medalhas,numero_olimpiadas_disputadas)
                    ni = ni+1
                else:
                    print("Maximos de atletas cadastrados")


            elif ec == 3 :
                if mi < 1:
                    print("~"*30)
                    print("Cadastrar Lutador de MMA:")
                    nome = input('Digite o nome: ') 
                    idade = int(input('Digite sua idade: '))
                    categoria_de_peso = input('categoria de peso: ')
                    cinturoes_disputados = int(input('cinturoes disputados: '))
                    LU = LutadorMMA(nome, idade,categoria_de_peso,cinturoes_disputados)
                    mi = mi+1
                else:
                    print("Maximos de atletas cadastrados")

            elif ec == 0:
                print('voltando ao menu principal....')


    elif op == 2:
        while most!= 0:
            print(' Mostrar Informação de atleta')
            print('Qual deseja mostrar: \n[1] - Mostrar Futebolista\n[2] - Mostrar Nadador\n[3] - Mostrar Lutador de MMA\n[0] - Retornar ao menu anterior')
            most = int(input('Qual sua opçao: '))
            if most == 1:
                print('Mostrar Futebolista')
                print(b.faz_o_que(b.nome, b.gols))

            elif most == 2:
                print('Mostrar Nadador')
                print(P.faz_o_que(P.nome, P.numero_de_medalhas, P.numero_olimpiadas_disputadas))
                
            elif most == 3:
                print('Mostrar Lutador de MMA')
                print(LU.faz_o_que(LU.nome, LU.categoria_de_peso, LU.cinturoes_disputados))

            elif most == 0:
                print('voltando ao menu principal....')

    else:
        print("\n finalizando....\n")