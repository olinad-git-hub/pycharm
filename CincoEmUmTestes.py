
from time import sleep
from random import randint, sample
from emoji import emojize

class Todas():
    def __init__(self):
        self.msg = 'ALGUNS PROGRAMAS PARA TREINO RAPIDO (BEGINNER)! '
        self.menutodos = ''' 
        1 - CALCULADORA
        2 - TABUADA
        3 - ADVINHE
        4 - MEGA SENA
        5 - MEDIA ALUNO
        6 - SAIR
        '''
        self.repet = True


    def Iniciar(self):
        while self.repet == True:
            try:
                print('*' * 50)
                print(self.msg)
                print('*' * 50)
                print(self.menutodos)
                opc = int(input('INFORME A OPÇÃO DESEJADA: '.center(30)))
                Linha()
                if opc == 1:
                    Calculadora()
                    continue
                elif opc == 2:
                    Tabuada()
                    continue
                elif opc == 3:
                    MaiorMenor()
                    continue
                elif opc == 4:
                    MegaSena()
                    continue
                elif opc == 5:
                    Media()
                    continue
                elif opc == 6:
                    print (emojize('\033[31:7mF I M :warning: \033[m',use_aliases=True))
                    self.repet = False
                elif opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5 and opc!= 6:
                    print('\033[31:1:7mOPS! NÃO TEM ESSE NUMERO NO MENU!\033[m')
                    continue
            except ValueError:
                print('\033[31:1:7mSOMENTE NUMEROS!\033[m')

def Linha():
    print('='*35)

def Calculadora():
    print('       \033[1:35:7mC A L C U L A D O R A\033[m'.center(33))
    Linha()
    print(f''' 
    1 - SOMA
    2 - SUBTRAÇÃO
    3 - MULTIPLICAÇÃO
    4 - DIVISÃO
    5 - SAIR
    ''')
    while True:
        try:
            escolha = int(input('\033[1:7mEscolha o operador que deseja usar:\033[m '))
            if escolha == 5:
                break
            elif escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5:
                print('\033[7:31mERRO! Numero de 1 a 5\033[m')
                continue
        except ValueError:
            print('\033[7:31mOps! Letra não pode!\033[m')
            continue
        while True:
            try:
                n1 = float(input('Escolha um Numero: '))
            except ValueError:
                print('\033[7:31mSomente Numeros\033[m')
                continue

            while True:
                try:
                    n2 = float(input('Escolha outro Numero: '))
                except ValueError:
                    print('\033[7:31mSomente Numeros\033[m')
                    continue
                if escolha == 1:
                    soma = (n1 + n2)
                    print(f' Sua escolha foi a \033[7mSOMA\033[m, e os numeros escolhidos foram-> {n1} + {n2} = {soma:.2f}')

                elif escolha == 2:
                    subtracao = (n1 - n2)
                    print(f' Sua escolha foi a \033[7mSUBTRAÇÃO\033[m, e os numeros escolhidos foram-> {n1} - {n2} = {subtracao:.2f}')

                elif escolha == 3:
                    multiplicacao = (n1 * n2)
                    print(f' Sua escolha foi a \033[7mMULTIPLICAÇÃO\033[m, e os numeros escolhidos foram-> {n1} * {n2} = {multiplicacao:.2f}')

                elif escolha == 4:
                    divisao = (n1 / n2)
                    print(f' Sua escolha foi a \033[7mDIVISÃO\033[m, e os numeros escolhidos foram-> {n1} / {n2} = {divisao:.2f}')
                break
            break

def Tabuada():
    print('           \033[1:30:7mT A B U A D A\033[m'.center(33))
    Linha()

    while True:
        try:
            num = int(input('\033[1:32mEscolha um numero para saber a Tabuada:\033[m '))
        except ValueError:
            print('\033[7:30mERRO! Somente numeros!\033[m')
            continue
        for cont in range(1,11):
            print(f'{num} X {cont}= {cont*num} ')
        Linha()
        op = str(input('\033[1:32mDeseja ver outra Tabuada? [s/n]:\033[m '))
        if op == 's':
            continue
        elif op == 'n':
            break
        elif op != 's' and op != 'n':
            print('\033[1:31mErro de Digitação!\033[m')
            continue

def MaiorMenor():
    cont = 0
    sorteio = randint(1,10)
    print('     \033[1:7:34mCHUTE UM NUMERO DE 0 A 10\033[m')
    Linha()
    while True:
        try:
            chute = int(input('Chute o Numero: '))
            cont += 1
            if chute > sorteio:
                print('Chute menos..')
            elif chute < sorteio:
                print('Chute mais..')
            elif chute == sorteio:
                print(f'\033[1:34mParabens vc acertou na {cont}º tentativa!\033[m')
                break
        except ValueError:
            print('\033[1:31:7mErro! Chute apenas Numeros!\033[m')
            continue

def MegaSena():
    print('           \033[1:33:7mM E G A_S E N A\033[m'.center(33))
    Linha()
    while True:
        opcao = str(input('Deseja Sortear um jogo da \033[33mMega Sena\033[m [s/n]: '))
        if opcao != 's' and opcao != 'n':
            print('\033[1:31:7mErro! Somente [s/n]\033[m')
            continue
        elif opcao == 's':
            sorte = sample(range(1, 60), 6)
            print(f'Seu jogo sorteado foi: \033[1:7m{sorte}\033[m')
            continue
        elif opcao == 'n':
            break

def Media():
    print('         \033[1:7mM E D I A_N O T A\033[m'.center(33))
    Linha()
    while True:
        try:
            nota1 = float(input('Digite a Primeira nota: '))
        except ValueError:
            print('\033[31:7mErro Somente Numero!\033[m')
            continue
        while True:
            try:
                nota2 = float(input('Digite a Segunda Nota: '))
            except ValueError:
                print('\033[1:31:7mErro Somente Numero!\033[m')
                continue
            media = (nota1 + nota2) / 2
            if media >= 7:
                print(f'\033[1:33mPARABÉNS APROVADO COM MEDIA:\033[m {media:.2f}')
            elif media <= 4.9:
                print(f'\033[1:31mREPROVADO! COM MEDIA:\033[m {media:.2f}')
            elif media > 5 or media <=6:
                print(f'\033[1:32mATENÇÃO! RECUPERAÇÃO COM MEDIA:\033[m {media:.2f}')
            break
        opcao = str(input('\033[1:7mDeseja ver mais algulma Media? [s/n]:\033[m '))
        if opcao == 's':
            continue
        elif opcao == 'n':
            break
        elif opcao != 's' and opcao != 'n':
            print('\033[31:1:7mERRO na Digitação!\033[m')
            continue

tod = Todas()
tod.Iniciar()







