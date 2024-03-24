from pymongo import MongoClient
from bson.objectid import ObjectId
from model_livros import ModelLivros


def menu():
    print("Menuzinho dos livros:")
    print("1. Cria um novo livro")
    print("2. Lê um novo livro usando seu ID")
    print("3. Atualiza um livro, ele é encontrado pelo ID")
    print("4. Deleta um livro pelo ID")
    print("5. Sair")


def menu_livros(database):

    livros = ModelLivros(database)

    while True:
        menu()
        opcao = input("Escolha a opção desejada: ")

        if opcao == "1":
            print("Entre com o titulo do livro: ")
            titulo = str(input())
            print("Entre com o autor: ")
            autor = str(input())
            print("Entre o ano do livro: ")
            ano = int(input())
            print("Entre o preço do livro: ")
            preco = float(input())
            livros.create_livro(titulo=titulo, autor=autor, ano=ano, preco=preco)

        elif opcao == "2":
            print("Entre o ID do livro que você quer procurar: ")
            id = input()
            livros.read_livro(id)
        
        elif opcao == "3":
            print("Entre o ID do livro a ser atualizado:")
            id = input()
            print("Agora entre com os atributos do livro \n")
            print("Entre com o titulo do livro: ")
            titulo = str(input())
            print("Entre com o autor: ")
            autor = str(input())
            print("Entre o ano do livro: ")
            ano = int(input())
            print("Entre o preço do livro: ")
            preco = float(input())
            livros.update_livro(id,titulo,autor,ano,preco)
        
        elif opcao == "4":
            print("Entre com o ID do livro a ser deletado: ")
            id = input()
            livros.delete_livro(id)

        elif opcao == "5":
            break

        else:
            print("Escolha incorreta, por favor escolha uma opção válida")