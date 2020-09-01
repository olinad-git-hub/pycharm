from emoji import emojize
print()
print(emojize(f'\033[1:7:34mC A L C U L A D O R A (:heavy_minus_sign: :heavy_plus_sign: '
              f':heavy_division_sign: :heavy_multiplication_x:)\033[m', use_aliases=True).center(50))
print()

class Calculadora():
    def __init__(self):
        self.primeiro ='Digite o PRIMEIRO Numero!: '
        self.segundo ='Digite o SEGUNDO Numero!: '
        self.oper =(emojize('QUAL OPERADOR DESEJA UTILIZAR?\033[1:31m (:heavy_minus_sign: '
                            ' :heavy_plus_sign: ' f'/ *)'
                            f'\033[m:', use_aliases=True))

    def Iniciar(self):
        while True:
            try:
                self.num1 = int(input(self.primeiro))
            except:
                print('\033[1:7mOpção Invalida! Somente Numeros!\033[m')
                continue
            while True:
                try:
                    self.num2 = int(input((self.segundo)))
                except:
                    print('\033[1:7mOpção Invalida! Somente Numeros!\033[m')
                    continue
                while True:
                    try:
                        self.operacao = str(input(self.oper))
                        if self.operacao == '+':
                            return self.Soma()
                        elif self.operacao == '-':
                            return self.Subtra()
                        elif self.operacao == '*':
                            return self.Multiplica()
                        elif self.operacao == '/':
                            return self.Divisao()
                    except:ValueError
                    print('\033[1:7:31mOps! Somente Operadores\033[m')
                    continue


    def Soma(self): #soma
           soma = (self.num1 + self.num2)
           print(f'Você optou pela operação (\033[1:32mSOMA\033[m)'
                 f' o resultado de {self.num1} + {self.num2} = {soma:.2f}')
           self.Linhas()
           self.Repetir()

    def Subtra(self):  # Menos
        subtra = self.num1 - self.num2
        print(f'Você optou pela operação (\033[1:32mSUBTRAÇÃO\033[m)'
              f' o resultado de {self.num1} - {self.num2} = {subtra:.2f}')
        self.Linhas()
        self.Repetir()

    def Multiplica(self): #Multiplicação
           multiplica = self.num1 * self.num2
           print(f'Você optou pela operação (\033[1:32mMULTIPLICAÇÃO\033[m)'
                 f' o resultado de {self.num1} * {self.num2} = {multiplica:.2f}')
           self.Linhas()
           self.Repetir()

    def Divisao(self):  #Divisão
        divi = self.num1 / self.num2
        print(f'Você optou pela operação (\033[1:32mDIVISÃO\033[m)'
              f' o resultado de {self.num1} / {self.num2} = {divi:.2f}')
        self.Linhas()
        self.Repetir()

    def Repetir(self):
        while True:
            try:
                self.repete = str(input('Deseja Realizar mais alguma operação? [s/n]: ')).upper().strip()[0]
            except:
                print('\033[1:7mOpção incorreta, somente [s/n]: \033[m')
                continue
            if self.repete != 'S' and self.repete != 'N':
                print('\033[1:7mOpção Invalida!, somente [s/n]: \033[m')
                continue
            elif self.repete == 'S':
               self.Iniciar()
            elif self.repete == 'N':
                print(emojize('\033[1:31mFIM do Programa\033[m :lock:',use_aliases=True))
                self.Linhas()
            break

    def Linhas(self):
        print('='*66)

calc= Calculadora()
calc.Iniciar()
