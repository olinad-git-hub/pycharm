from random import randint

class Chute():
    def __init__(self):
        self.chute_min = 1
        self.chute_max = 25
        self.aleatorio = 0
        self.tentar_novamente = True

    def GerarNumeroAleatorio(self):
        self.aleatorio = randint(self.chute_min,self.chute_max)

    def PedirNumero(self):
        self.chute = int(input('Chute um numero: '))

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirNumero()
        try:
            while self.tentar_novamente == True:
                if self.chute > self.aleatorio:
                    print('Chute um valor \033[1;31mMENOR\033[m..')
                    self.PedirNumero()
                elif self.chute < self.aleatorio:
                    print('Chute um valor \033[1;32mMAIOR\033[m')
                    self.PedirNumero()
                if self.aleatorio == self.chute:
                    print(f'parabens vc acertou')
                    op = input(f'Gostaria de jogar de novo: [s/n]: ')
                    if op == 's':
                      self.GerarNumeroAleatorio()
                      self.PedirNumero()
                    if op == 'n':
                        self.tentar_novamente = False
                        print('Fim do programa!')
        except:
            print('Favor digitar somente numero')
            self.PedirNumero()



sorte = Chute()
sorte.Iniciar()

