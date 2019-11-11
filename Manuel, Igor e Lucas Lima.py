class funcionario():
    __instance = None

    def __init__(self, nome, salario, cargo, mestrab):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.mestrab = mestrab


    def print_nome(self):
        print(self.nome)

    def print_cargo(self):
        print(self.cargo)

    def print_salario(self):
        print(self.salario)

    def calc_13D(self):
       return self.salario * self.mestrab / 12

    def print_tudo(self):
        print("\n")
        print("Nome:", self.nome, "- Salario:", self.salario, "- Cargo:", self.cargo, "- Decimo 13º:", self.calc_13D())


nome = input("digite seu nome: ")
salario = int(input("digite seu salario: "))



cargo = input("digite seu cargo: ")
mesTrab = int(input("digite quantos meses de trabalho voce tem: "))

gerente = funcionario(nome, salario, cargo, mesTrab)
gerente.print_tudo()
