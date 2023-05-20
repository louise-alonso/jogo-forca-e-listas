                                                                    #Jogo Forca:
"""Está abrindo o diretório 'pycache' e eu não sei como resolver.
Já coloquei 'set PYTHONDONTWRITEBYTECODE=1', mas não funcionou .
No entanto, isso não afeta o funcionamento do jogo. """
import random
from art import estagios, logo
from palavras import lista_palavras

tema_escolhido = random.choice(list(lista_palavras.keys()))
palavra_escolhida = random.choice(lista_palavras[tema_escolhido])
tamanho_palavra = len(palavra_escolhida)

fim_do_jogo = False
vidas = 6

print(logo)

print(f'\nPssst, a palavra está relacionada ao tema "{tema_escolhido}".\n')
print("Adivinhe a palavra!\n")

display = []
for _ in range(tamanho_palavra):
    display += "_"

letras_erradas = []

while not fim_do_jogo:
    palpite = input("Adivinhe uma letra: ").lower()

    if palpite in display or palpite in letras_erradas:
        print(f"Você já adivinhou a letra {palpite}.")
    elif palpite in palavra_escolhida:
        for posicao in range(tamanho_palavra):
            letra = palavra_escolhida[posicao]
            if letra == palpite:
                display[posicao] = letra
    else:
        print(f"A letra {palpite} não está na palavra. Você perde uma vida.")
        vidas -= 1
        letras_erradas.append(palpite)
        if vidas == 0:
            fim_do_jogo = True
            print("Você perdeu.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        fim_do_jogo = True
        print("Parabéns! Você acertou a palavra.")

    print(estagios[6 - vidas])
