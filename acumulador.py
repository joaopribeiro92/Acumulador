# Acumulador:

num1 = int(input('Entre com o valor inicial: '))
num2 = int(input('Entre com o valor final: '))
soma = 0

while (num1 - 1) <= (num2 - 1):
    if num1 % 2 == 0:
        soma += num1
    num1 += 1
    print(num1)
    print()
print('A soma:', soma)


