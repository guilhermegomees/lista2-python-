"""
    (Desafio) Faça um programa que apresenta a tabuada completa de 1 a 10.
"""

numA = 0

while numA < 10:
    print('')
    numA += 1
    numB = 0
    while numB < 10:
        numB += 1
        print(str(numA) + ' X ' + str(numB) + ' = ' + str(numA * numB))