                                                                        #Lista de exercícios - Estrutura Sequencial:

'''1. Faça um programa que converta metros para centímetros.'''

metros = float(input( 'Digite o valor em metros a ser convertido em centímetros: '))
cm = metros*100

print(f'O valor em centímetros é de {cm}')


'''2. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''

raio = float(input('Digite o raio do círculo: '))
area = 3.14*(raio**2)

print(f'A área do círculo é de: {area:.2f}')


'''3. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro
desta área para o usuário.'''

lado = float(input('Digite a medida de um dos lados do quadrado: '))
area = lado ** 2
dobro_area = area * 2

print(f"A área do quadrado é {area:.2f}. O dobro da área é {dobro_area:.2f}.")


'''4. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input('Digite o número de horas trabalhadas no mês: '))

salario = valor_hora * horas_trabalhadas

print(f'O seu salário no mês é R${salario:.2f}.')


'''5. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
a temperatura em graus Celsius.'''
#1. C = 5 * ((F-32) / 9).

fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
celsius = 5*((fahrenheit - 32) / 9)

print (f"A temperatura em graus Celsius é: {celsius :.2f}")


'''6. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em
graus Fahrenheit.'''

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 1.8) + 32

print ("A temperatura em graus Fahrenheit é: {:.2f}".format(fahrenheit))


'''7. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:'''
#1. o produto do dobro do primeiro com metade do segundo .
#2. a soma do triplo do primeiro com o terceiro.
#3. o terceiro elevado ao cubo.

n1 = float(input("Digite um número inteiro: "))
n2 = float(input("Digite mais um número inteiro: "))
n3 = float(input("Digite um número real: "))

resultado1 = (n1 * 2) * (n2/2)
resultado2 = (n1 * 3) + n3
resultado3 = n3 **3

print ("O produto entre o dobro do primerio número e a metade do segundo número:4",resultado1 )
print ("A soma entre o triplo do primeiro número e o terceiro número:",resultado2)
print ("O terceiro número elevado ao cubo:",resultado3)


'''8. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

altura = float(input("Digite sua altura: "))
peso = (72.7 * altura) - 58

print (f"seu peso ideial é: {peso :.2f}")


'''9. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
calcule seu peso ideal, utilizando as seguintes fórmulas:'''
#1. Para homens: (72.7*h) - 58
#2. Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M para masculino ou F para feminino): ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal:.2f} kg")
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso_ideal:.2f} kg")
else:
    print("Sexo inválido, digite M ou F.")
