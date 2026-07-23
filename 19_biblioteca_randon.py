# Programa que lê os nomes de quatro alunos e sorteie um.

import random
lista = []
a1 = lista.append(str(input('Digite o primeiro nome: ')))
a2 = lista.append(str(input('Digite o segundo nome: ')))
a3 = lista.append(str(input('Digite o terceiro nome: ')))
a4 = lista.append(str(input('Digite o quarto nome: ')))

#lista = [a1, a2, a3, a4] # esta forma seria sem usar o append
# tem que criar uma lista para que a função execute. Uma lista fica sempre entre [] cochetes.

print('O nome escolhido foi -->> {}'.format(random.choice(lista)))  
# o módulo 'choice' escolha em inglês.