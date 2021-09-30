"""
    Faça um programa que leia 5 números e informe a soma e a média dos números
"""
num = 0

for i in range(5):
    num += float(input("NUMERO: "))

print("SOMA: ", num)
print("MEDIA: ", num / 5)