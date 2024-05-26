#não sei porque mas depois de mudar um parenteses meu código quebrou de rodar aqui no vscode diretamente pelo botão de run
# eu desfiz o que eu tinha feito que causou isso mas continuou
#mas se abrir o terminal do vscode, ir até a pasta que os arquivos estão salvos, e usar "python main.py" o código roda perfeitamente
from database import Database
from query import questao_1, questao_2
from teacher_crud import TeacherCRUD
from teacher_cli import TeacherCLI

#criando a instancia da classe Database, que faz a conexão com o neo4j
db = Database("bolt://18.206.90.55:7687", "neo4j", "catchers-chairs-seamen")


#execução das queries das questões 1 e 2
quest_1 = questao_1(db)
print("Questão 1 -Letra A")
quest_1.letra_a()
print("Questão 1 -Letra B")
quest_1.letra_b()
print("Questão 1 -Letra C")
quest_1.letra_c()
print("Questão 1 -Letra D")
quest_1.letra_d()

quest_2 = questao_2(db)
print("Questão 2 -Letra A")
quest_2.letra_a()
print("Questão 2 -Letra B")
quest_2.letra_b()
print("Questão 2 -Letra C")
quest_2.letra_c()
print("Questão 2 -Letra D")
quest_2.letra_d()
#não sei se foi uma boa colocar na main, porque a cada vez que o código for rodado vai buscar tudo dnv

#execução da letra B, C e D da questão 3
teacherCRUD = TeacherCRUD(db)
teacherCRUD.create_teacher('Chris Lima', 1956, '189.052.396-66')
teacherCRUD.read_teacher('Chris Lima')
teacherCRUD.update_teacher('Chris Lima', '162.052.777-77')
#checando se a atualização deu certo
teacherCRUD.read_teacher('Chris Lima')

#execução do CLI
teacherCLI = TeacherCLI(teacherCRUD)
teacherCLI.run()