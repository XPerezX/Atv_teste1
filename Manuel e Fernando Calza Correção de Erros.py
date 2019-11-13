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

inputnome = False
inputsalario = False
inputcargo = False
inputmestrab = False

'''
salario = input("digite seu salario: ")
try:
    salario = float(salario)
except ValueError:
    print ("isso não é um numero")

print (type(salario))

'''

while inputnome == False:
    nome = input("digite seu nome: ")

    if all(str.isalpha(string) for string in nome.split()) and bool(nome.strip()) == True :
       _nome = nome
       inputnome = True
    else:
        print("O nome deve ser composto somente de caracteres")



while inputsalario == False:
    salario = input("digite seu salario: ")

    try:
        salario = float(salario)
    except ValueError:
        print ("isso não é um numero")

    if (isinstance(salario, float) is True) and salario > 0:
        _salario = salario
        inputsalario = True
    else:
        print("O salario deve ser um numero inteiro ou decimal maior que zero")

while inputcargo == False:

    cargo = input("digite seu cargo: ")
    if all(str.isalpha(string) for string in cargo.split()) and bool(cargo.strip()) == True :
        _cargo = cargo
        inputcargo = True
    else:
        print("O nome deve ser composto somente de caracteres")

while inputmestrab == False:
    mesTrab = input("digite quantos meses de trabalho voce tem: ")

    try:
        mesTrab = int(mesTrab)
    except ValueError:
        print ("isso não é um numero inteiro")


    if isinstance(mesTrab, int) == True and mesTrab > 0:
        _mestrab = mesTrab
        inputmestrab = True
    else:
        print("Os meses de trabalho devem ser inteiros e maiores que zero")

gerente = funcionario(_nome, _salario, _cargo, _mestrab)
gerente.print_tudo()



'''
                            Erro 1 ----CORRIGIDO----    saida = "O nome deve ser composto somente de caracteres"
                                        
                                        
Erro 1 - Recebe nome como numero                                 
(digite seu nome: 5
digite seu salario: 2000
digite seu cargo: Uber
digite quantos meses de trabalho voce tem: 12
Nome: 5 - Salario: 2000 - Cargo: Uber - Decimo 13º: 2000.0
Process finished with exit code 0)
                    
                        Erro 2 ----CORRIGIDO---- saida = "O nome deve ser composto somente de caracteres"
                                        
Erro 2 - Nome recebe caractere especial                         
(digite seu nome: ***
digite seu salario: 3000
digite seu cargo: Camioneiro
digite quantos meses de trabalho voce tem: 12
Nome: *** - Salario: 3000 - Cargo: Camioneiro - Decimo 13º: 3000.0
Process finished with exit code 0)

                    Erro 3 ----CORRIGIDO----  saida = "O nome deve ser composto somente de caracteres"
                                     
Erro 3 - Nome recebe espaço em branco                         
(digite seu nome: 
digite seu salario: 3000
digite seu cargo: japoegj
digite quantos meses de trabalho voce tem: 12
Nome:  - Salario: 3000 - Cargo: japoegj - Decimo 13º: 3000.0
Process finished with exit code 0)
                                
                 Erro 4 -   ----CORRIGIDO----        saida = "isso não é um numero"
                                 
Erro 4 - Não exibe mensagem de " Por favor digite um numero " no teste do salario quando inserido caracter, da erro de console.
(digite seu nome: Ratinho
digite seu salario: Leptospirose
Traceback (most recent call last):
File "C:/Users/Desenvolvimento/PycharmProjects/Testes11/11/19/testando.py", line 29, in <module>
salario = int(input("digite seu salario: "))
ValueError: invalid literal for int() with base 10: 'Leptospirose'
Process finished with exit code 1)

                Erro 5 ----CORRIGIDO----        saida = "isso não é um numero"
                                        
Erro 5 - Não exibe mensagem de " Por favor digite um numero " no teste do salario quando inserido caracter especial, da erro de console.
(digite seu nome: FERNANDO
digite seu salario: #$&(*!&#
Traceback (most recent call last):
File "C:/Users/Desenvolvimento/PycharmProjects/Testes11/11/19/testando.py", line 29, in <module>
salario = int(input("digite seu salario: "))
ValueError: invalid literal for int() with base 10: '#$&(*!&#'
Process finished with exit code 1)

            Erro 6 ----CORRIGIDO----     saida = "O salario deve ser um numero inteiro ou decimal maior que zero"
                                    
Erro 6 - Não exibe mensagem de " Por favor digite um numero " no teste do salario quando deixado em branco, da erro de console
(digite seu nome: aids
digite seu salario: 
Traceback (most recent call last):
File "C:/Users/Desenvolvimento/PycharmProjects/Testes11/11/19/testando.py", line 29, in <module>
salario = int(input("digite seu salario: "))
ValueError: invalid literal for int() with base 10: ''
Process finished with exit code 1)

         Erro 7 ----CORRIGIDO----   saida = O salario deve ser um numero inteiro ou decimal maior que zero
                                    
Erro 7 - Recebe salário como negativo
(digite seu nome: kkkjj
digite seu salario: -39218
digite seu cargo: kpop
digite quantos meses de trabalho voce tem: 12
Nome: kkkjj - Salario: -39218 - Cargo: kpop - Decimo 13º: -39218.0
Process finished with exit code 0)


 Erro 8 ----CORRIGIDO----  saida = O salario deve ser um numero inteiro ou decimal maior que zero ou "Os meses de trabalho devem ser inteiros e maiores que zero"
                                    
Erro 8 - Calculo de decimo terceiro aceita negativo
(digite seu nome: Mijo na gaveta
digite seu salario: 3232
digite seu cargo: punheteiro
digite quantos meses de trabalho voce tem: -12
Nome: Mijo na gaveta - Salario: 3232 - Cargo: punheteiro - Decimo 13º: -3232.0
Process finished with exit code 0)

                 Erro 9 ----CORRIGIDO---- saida = Os meses de trabalho devem ser inteiros e maiores que zero
                                    
Erro 9 - Não exibe mensagem de " Por favor digite os meses " no teste do decimo terceiro quando deixado em branco, da erro de console 
(digite seu nome: Le park
digite seu salario: 12309
digite seu cargo: jef
digite quantos meses de trabalho voce tem: 
Traceback (most recent call last):
File "C:/Users/Desenvolvimento/PycharmProjects/Testes11/11/19/testando.py", line 34, in <module>
mesTrab = int(input("digite quantos meses de trabalho voce tem: "))
ValueError: invalid literal for int() with base 10: ''
Process finished with exit code 1)

                     Erro 10 ----CORRIGIDO---- saida = isso não é um numero inteiro
                                
Erro 10 - Não exibe mensagem de " Por favor digite os meses " no teste do decimo terceiro quando inserido caracter especial, da erro de console 
(digite seu nome: paep
digite seu salario: 12093
digite seu cargo: asi
digite quantos meses de trabalho voce tem: *(&$*
Traceback (most recent call last):
File "C:/Users/Desenvolvimento/PycharmProjects/Testes11/11/19/testando.py", line 34, in <module>
mesTrab = int(input("digite quantos meses de trabalho voce tem: "))
ValueError: invalid literal for int() with base 10: '*(&$*'
Process finished with exit code 1)

                Erro 11 ----CORRIGIDO----  saida = Os meses de trabalho devem ser inteiros e maiores que zero
                                    
Erro 11 - Não exibe mensagem de " Por favor digite os meses corretamente" no teste do decimo terceiro quando inserido meses negativos, da erro de console
(digite seu nome: barril
digite seu salario: 091824
digite seu cargo: corno
digite quantos meses de trabalho voce tem: -12
Nome: barril - Salario: 91824 - Cargo: corno - Decimo 13º: -91824.0
Process finished with exit code 0)

                Erro 12 ----CORRIGIDO----  saida = O nome deve ser composto somente de caracteres
                                    
Erro 12 - Recebe cargo como numero
(digite seu nome: culote
digite seu salario: 92039
digite seu cargo: 3827198
digite quantos meses de trabalho voce tem: 12
Nome: culote - Salario: 92039 - Cargo: 3827198 - Decimo 13º: 92039.0
Process finished with exit code 0)

                 Erro 13 ----CORRIGIDO---- saida = O nome deve ser composto somente de caracteres
                                
Erro 13 - Recebe cargo como nulo (em branco)
(digite seu nome: antonio
digite seu salario: 21838
digite seu cargo: 
digite quantos meses de trabalho voce tem: 12
Nome: antonio - Salario: 21838 - Cargo:  - Decimo 13º: 21838.0
Process finished with exit code 0)

                 Erro 14 ----CORRIGIDO---- saida = O nome deve ser composto somente de caracteres
                            
Erro 14 - Recebe cargo como caracter especial
(digite seu nome: falta 4
digite seu salario: 1238
digite seu cargo: &&&&
digite quantos meses de trabalho voce tem: 12
Nome: falta 4 - Salario: 1238 - Cargo: &&&& - Decimo 13º: 1238.0
Process finished with exit code 0)

                                 ----Não Pertinente------
                          
Erro 15 - Decimo terceiro não emite alert quando menor que 12  (não pertinente)
(digite seu nome: foepiuh
digite seu salario: 29183
digite seu cargo: jpaegjd
digite quantos meses de trabalho voce tem: 3
Nome: foepiuh - Salario: 29183 - Cargo: jpaegjd - Decimo 13º: 7295.75
Process finished with exit code 0)

             Erro 16 ----CORRIGIDO----         saida = Os meses de trabalho devem ser inteiros e maiores que zero
                        
Erro 16 - Decimo terceiro não emite alert quando negativo
(digite seu nome: jeopaij
digite seu salario: 9348
digite seu cargo: aeidgj
digite quantos meses de trabalho voce tem: -12
Nome: jeopaij - Salario: 9348 - Cargo: aeidgj - Decimo 13º: -9348.0
Process finished with exit code 0)


     Erro 17 ----CORRIGIDO---- saida = isso não é um numero O salario deve ser um numero inteiro ou decimal maior que zero
                            
Erro 17 - Salario da erro de console quando nulo
(digite seu nome: feaf
digite seu salario: 
Traceback (most recent call last):
File "C:/Users/Desenvolvimento/PycharmProjects/Testes11/11/19/testando.py", line 29, in <module>
salario = int(input("digite seu salario: "))
ValueError: invalid literal for int() with base 10: ''
Process finished with exit code 1)


'''