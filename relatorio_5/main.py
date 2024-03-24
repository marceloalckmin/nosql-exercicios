from database import Database
from model_livros import ModelLivros
from menu_livros import menu_livros

db = Database(database='relatorio_5',collection='Livros')

#model_livros = ModelLivros(database=db)
#criando livros
#model_livros.create_livro("1984","George Owell", 1949, 22.95)
#lendo livros(o objeto)
#model_livros.read_livro("660096c85863c7dc400f37e3")
#atualizando livros
#model_livros.update_livro("660096c85863c7dc400f37e3", "Meditações", "Marco Aurélio", 175, 30)
#deletando livros
#model_livros.delete_livro("660096c85863c7dc400f37e3")

menu_livros(db)
