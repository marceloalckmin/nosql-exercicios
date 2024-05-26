class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class TeacherCLI(SimpleCLI):
    def __init__(self, TeacherCRUD):
        super().__init__()
        self.TeacherCRUD = TeacherCRUD
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Entre com o nome do professor: ")
        ano_nasc = input("Entre com o ano de nascimento do professor: ")
        cpf = input("Entre com o cpf do professor: ")
        self.TeacherCRUD.create_teacher(name, ano_nasc, cpf)

    def read_teacher(self):
        name = input("Entre com o nome do professor que deseja procurar: ")
        self.TeacherCRUD.read_teacher(name)

    def update_teacher(self):
        name = input("Entre com o nome do professor que deseja atualizar: ")
        newCpf = input("Entre com o cpf que será colocado no lugar do atual: ")
        self.TeacherCRUD.update_teacher(name, newCpf)

    def delete_teacher(self):
        name = input("Entre com o nome do professor que deseja deletar: ")
        self.TeacherCRUD.delete_teacher(name)