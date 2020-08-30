from emoji import emojize
from random import randint
from boneco_forca import boneco

def jogada(result):
    if result == 6:
        print(emojize( ':o: :o: :o:\n'
                       ':o: :o: :o:', use_aliases=True))
        boneco(6)
    elif result == 5:
        print(emojize(':o: :o: \n'
                      ' :o:\n'
                      ':o: :o: ', use_aliases=True))
        boneco(5)
    elif result == 4:
        print(emojize(':o: :o:\n'
                      ':o: :o: ', use_aliases=True))
        boneco(4)

    elif result == 3:
        print(emojize( ':o: \n'
                       '  :o: \n'
                       '    :o:', use_aliases=True))
        boneco(3)

    elif result == 2:
        print(emojize( ':o: \n'
                       '     \n'
                       '    :o:', use_aliases=True))
        boneco(2)

    elif result == 1:
        print(emojize( '     \n'
                       '  :o: \n'
                       '    ', use_aliases=True))
        boneco(1)

class Dado:
    def __init__(self):
        self.valor_min = 1
        self.valor_max = 6
        self.mensagem = 'Deseja jogar o dado novamente? '

    def Iniciar(self):
            resposta = input(self.mensagem).strip().upper()
            if resposta == 'SIM':
                v = randint(self.valor_min, self.valor_max)
            if v == 1:
                return jogada(1)
            elif v == 2:
                return jogada(2)
            elif v == 3:
                return jogada(3)
            elif v == 4:
                return jogada(4)
            elif v == 5:
                return jogada(5)
            elif v == 6:
                return jogada(6)




simulador = Dado()
while True:
    simulador.Iniciar()







