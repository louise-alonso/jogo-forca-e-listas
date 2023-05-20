                                            #LISTA ESTRUTUTA DE DECISÃO

'''1)Solicite ao usuário um valor numérico, inteiro ou real, e verifique se ele é maior ou
menor que 10. O programa deve escrever a mensagem correspondente (maior ou
menor) e informar o valor digitado pelo usuário.'''

valor= float(input('Digite um valor: '))

if valor > 10:
    print('O valor digitado é maior que 10')
else:
    print('O valor digitado é menor que 10')
print(f'O valor digitado foi {valor}')


'''2. Solicite ao usuário um valor numérico, inteiro ou real, e escrever se é positivo ou
negativo (considere o valor zero como positivo).'''

valor= float(input('Digite um valor: '))

if valor >= 0:
    print('O valor digitado é postivo')
else:
    print('O valor digitado é negativo')


'''3. As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
compradas, calcule e escreva o custo total da compra.'''

numero_maça= int(input('Digite a quantidade de maçãs '))

if numero_maça <12:
    custo =  numero_maça* 1.30
else:
    custo = numero_maça* 1.0
print(f'O valor total da compra é {custo :.2f}')


'''4. Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples
e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que
nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.'''

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2

if media >=6:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado')
print(f'Sua media foi: {media :.2}')


'''5. Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
deles.'''

valor1= float(input('Digite o primeiro numero: '))
valor2= float(input('Digite o segundo numero: '))

if valor1 > valor2:
    print('O primeiro valor é maior que o segundo')
else:
    print('Osegundo valor é maior que o primeiro')


'''6. Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em
ordem crescente.'''

valor1= float(input('Digite o primeiro numero: '))
valor2= float(input('Digite o segundo numero: '))

if valor1 > valor2:
    print('A ordem crescente é ',valor2 , valor1)
else:
    print('A ordem crescente é ',valor1 , valor2)


'''7. Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
senão escrever a mensagem 'Saldo Negativo'.'''

numero_conta = input("Digite o número da conta: ")
saldo = float(input("Digite o saldo da conta: "))
debito = float(input("Digite o débito da conta: "))
credito = float(input("Digite o crédito da conta: "))

saldo_atual = saldo - debito + credito

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
print("Saldo atual:", saldo_atual)


'''8. Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.'''

quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
quantidade_maxima = int(input("Digite a quantidade máxima em estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima em estoque: "))
quantidade_media = (quantidade_maxima + quantidade_minima) / 2

if quantidade_atual >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")


'''9. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
conceito for D ou E.'''

nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Média:", media)
print("Conceito:", conceito)

if conceito in ("A", "B", "C"):
    print("APROVADO")
else:
    print("REPROVADO")