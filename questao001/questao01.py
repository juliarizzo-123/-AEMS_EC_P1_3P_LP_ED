
from collections import Counter
import os
os.chdir("C:\\Users\\Julia\\Documents\\faculdade\\PROVA1\\env001\\questao001\\")

soneto = open ('quest.txt', "r")
data = soneto.read()
numdepala = len(data.split())
print("~~"*30)

print ("O numero de palavras é: {}".format(numdepala))
print("~~"*30)