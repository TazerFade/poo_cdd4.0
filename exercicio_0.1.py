from biblioteca import ListaNomes

def main():
    lista = ListaNomes()
    for i in range(5):
        nome = input(f"Digite o {i+1}º nome: ")
        lista.adicionar_nome(nome)

    nomes_com_a = lista.filtrar_nomes_com_a()
    print("\nNomes que começam com a letra 'A':")
    for nome in nomes_com_a:
        print(nome)

if __name__ == "__main__":
    main()
