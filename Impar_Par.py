from random import randint
from time import sleep
from tqdm import tqdm

def Linhas():
    print('='*30)

class ImparPar():
    def __init__(self):
        self.msg = 'Você escolhe PAR ou IMPAR? '
        self.numero = 'Qual numero?: '
        self.repetir = True

    def Iniciar(self):
        while self.repetir == True:
            impapar = input(self.msg).upper().strip()
            if impapar != 'PAR' and impapar != 'IMPAR':
                print('\033[1:31mOpção incorreta!\033[m')
                continue

            try:
                self.num = int(input(self.numero))
            except ValueError:
                print('\033[1:31mSomente Numeros!\033[m')
                continue

            self.op = randint(1, 10)
            print(f'Eu Escolho...')
            for i in tqdm(range(10)):
                sleep(.1)
            print(F'\033[1:32m{self.op}\033[m')
            if impapar == 'PAR' or impapar == 'IMPAR':
                result = (self.num + self.op)
                if result % 2 == 0:
                    print(f'Deu \033[1:31:40mPAR\033[m {self.num} + {self.op} = {result}')
                    Linhas()
                    denovo = str(input('Deseja jogar de novo? [s/n]: ')).lower().strip()
                    if denovo == 's':
                        continue
                    elif denovo != 's' and denovo != 'n':
                        print('\033[1:31mOpção incorreta!\033[m')
                        denovo = str(input('Deseja jogar de novo? [s/n]: ')).lower().strip()

                    elif denovo == 'n':
                        self.repetir = False
                        print('FIM DO JOGO')

                else:
                    print(f'Deu \033[1:31:40mIMPAR\033[m {self.num} + {self.op} = {result}')
                    Linhas()
                    denovo = str(input('Deseja jogar de novo? [s/n]: ')).lower().strip()
                    if denovo == 's':
                       continue
                    elif denovo != 's' and denovo != 'n':
                        print('\033[1:31mOpção incorreta!\033[m')
                        denovo = str(input('Deseja jogar de novo? [s/n]: ')).lower().strip()
                        continue

                    elif denovo == 'n':
                        self.repetir =False
                        print('FIM DO JOGO')


jogo = ImparPar()
jogo.Iniciar()


