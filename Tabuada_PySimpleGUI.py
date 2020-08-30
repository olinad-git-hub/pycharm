import PySimpleGUI as sg

class Tabuada():
    def __init__(self):
        layout = [
            [sg.Text('Informe o numero da tabuada: '), sg.Input(size=(15,0),key='numero')],
            [sg.Button('Mostrar'), sg.Button('Sair')],
            [sg.Output(size=(20,15))]
        ]


        self.janela = sg.Window('T A B U A D A'.center(20)).Layout(layout)


    def Iniciar(self):
        while True:
            self.button, self.valores = self.janela.read()
            num = int (self.valores['numero'])
            if self.button == 'Sair' or self.button == sg.WIN_CLOSED:
                break
            for c in range(1,11):
                print(f'{num} x {c} = {num*c}')
            Linhas()



def Linhas():
    print('='*17)



tabu = Tabuada()
tabu.Iniciar()