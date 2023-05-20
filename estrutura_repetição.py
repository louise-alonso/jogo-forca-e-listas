                                                         #Lista de exercícios - Estrutura de Repetição:

'''1.Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que, quando divididos por 11, produzam o resto igual a 5.'''

for num in range(1000, 2001):
    if num % 11 == 5:

        print(num)


'''2. Faça um programa que mostre as tabuadas dos números de 1 a 10.'''

for a in range(1, 11):

    print(f'Tabuada do {a}: ')

    for b in range(1, 11):
    

        print(f"{a} x {b} = {a*b}")


'''3. Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada pessoa acessando cada elemento da lista um de cada vez.'''

amigos = ["Luiz", "João", "Pedro", "Ana"]
for amigo in amigos:

    print(amigo)


'''4. Faça um programa que receba um número e que calcule e mostre a tabuada desse número.'''

num = int(input('Digite um número de 1 a 100: '))
for i in range(1, 101):

    print(f"{num} x {i} = {num*i}")


'''5. Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.'''

amigos = ["Luiz", "João", "Pedro", "Ana"]
for amigo in amigos:

    print(f'Olá {amigo}, como vai você?')

'''6. Seja criativo ao desenvolver este programa.
a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
d. Modifique sua lista, substitua os desistentes por novos convidados.
e. Exiba um novo convite para cada pessoa que continua presente em sua lista.'''

convidados = ['Christophen Nolan',  'Christian Bale', 'Leonardo DiCaprio', 'Billie Eilish', 'Jojo Todynho']

for convidado in convidados:
    print(f'\nOlá {convidado}, você está convidado para o meu jantar em casa amanhã\n')

nao_pode_ir = ["Leonardo DiCaprio"]

for nao_pode in nao_pode_ir:
    convidados = [convidado.replace(nao_pode, "Michael B. Jordan") for convidado in convidados]
    print(f'\nInfelizmente, {nao_pode} não poderá comparecer ao meu jantar.\n')

for convidado in convidados:
    print(f'\nOlá {convidado}, você está convidado para o meu jantar em casa no próximo sábado.\n')


'''7. Faça um cadastro de usuários com nome, idade e email, utilizando apenas o que você aprendeu até agora.'''
usuarios = []

while True:
    nome = input("Digite seu nome (ou 'cancelar' para encerrar o programa): ")

    if nome.lower() == "cancelar":
        if len(usuarios) == 0:
            print("\nOperação cancelada.\n")
            
        else:
            ver_dados = input("Deseja ver os dados cadastrados? (s/n) ")
            if ver_dados.lower() == "s":
                if len(usuarios) == 0:
                    print('\nNão há dados cadastrados\n')
                else:
                    print("\nDados cadastrados:\n")
                    for usuario in usuarios:
                        print(f"Nome: {usuario['nome']}\n Idade: {usuario['idade']}\n E-mail: {usuario['email']}\n")
            print('\nPode fechar o programa\n')

            break

    else:
        idade = int(input("Digite sua idade: "))
        email = input("Digite seu email: ")
        usuarios.append({"nome": nome, "idade": idade, "email": email})
        print("\nCadastro de usuário concluído com sucesso!\n")
    
    opcao = input("Deseja cadastrar outro usuário? (s/n) ")

    if opcao.lower() == "n":
        ver_dados = input("Deseja ver os dados cadastrados? (s/n) ")
        if ver_dados.lower() == "s":
            if len(usuarios) == 0:
                print('\nNão há dados cadastrados\n')

            else:
                print("\nDados cadastrados:\n")
                for usuario in usuarios:
                    print(f"Nome: {usuario['nome']}\nIdade: {usuario['idade']}\nE-mail: {usuario['email']}\n")

        print('\nPode fechar o programa\n')
        break
