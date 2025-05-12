class ListaNomes:
    def __init__(self):
        self.nomes = []

    def adicionar_nome(self, nome):
        self.nomes.append(Nome(nome))

    def filtrar_nomes_com_a(self):
        return [nome.nome for nome in self.nomes if nome.comeca_com_a()]

import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto}.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
