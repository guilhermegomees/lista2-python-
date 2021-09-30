"""
    Faça um programa que receba dois números 
    inteiros e gere os números inteiros que 
    estão no intervalo compreendido por eles.
"""

num1 = int(input("INFORME O PRIMEIRO NUMERO: "))
num2 = int(input("INFORME O SEGUNDO NUMERO: "))

while num2 < num1:
	num1 = int(input("INFORME O PRIMEIRO NUMERO: "))
	num2 = int(input("INFORME O SEGUNDO NUMERO: "))
else:
	for i in range(num1,num2,1):
		print(i)