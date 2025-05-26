#CRUD
#INTERFACE TEXTO
import time

def  adicionar_item():
    codigo = input ("Código do produto: ")
    descricao = input ("Descrição do produto: ")
    fabricante = input ("Fabricante: ")
    preco = input ("Preço: ")
    with open ("estoque.txt", "a", encoding= "utf-8") as arquivo:
        arquivo.write(f"{codigo},{descricao}, {fabricante}, {preco}\n")
    print("Item adicionado com sucesso! ")
    time.sleep(3)
def listar_estoque():
    print("Listar estoque")
    with open ("estoque.txt", "r", encoding= "utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            print(f" Código: {item[0]} | Descrição: {item[1]} Fabricante: {item[2]} | Preço: {item[3]}")

def alterar_item():
    print("Alterar item")
    codigo = input ("Digite o código do produto: ")

    with open ("estoque.txt", "r", encoding= "utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open ("estoque.txt", "w", encoding= "utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == codigo:
                print("Insira os novos dados: ")
                novo_codigo = input ("Codigo: ")
                nova_descricao = input ("Descrição: ")
                nova_fabricante = input ("Fabricante: ")
                novo_preco = input ("Preço: ")
                arquivo.write(f"{novo_codigo}, {nova_descricao}, {nova_fabricante}, {novo_preco}\n")
            else:
                print("Produto não localizado")
                arquivo.write(linha)
    time.sleep(3)
def remover_item():
    print("Remover item")
    codigo = input ("Digite o código do produto: ")
    with open ("estoque.txt", "r", encoding= "utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open ("estoque.txt", "w", encoding= "utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != codigo:
                arquivo.write(linha)
    time.sleep(3)


def menu():
    while True:
        print("\n ---- MENU ESTOQUE----")
        print("1 - Adicionar item ")
        print("2 - Listar estoque ")
        print("3 - Editar item ")
        print("4 - Remover item ")
        print("5 - Sair")
        opcao = int (input("Escolha uma opcao: "))
        if opcao == 1:
            adicionar_item()
        elif opcao == 2:
            listar_estoque()
        elif opcao == 3:
            alterar_item()
        elif opcao == 4:
            remover_item()
        elif opcao == 5:
            break
        else:
            print("Opcao invalida")
    time.sleep(3)
menu()