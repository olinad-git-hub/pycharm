import PySimpleGUI as sg

class Imc():
    def __init__(self):
        layout = [
            [sg.Text('Informe o seu Peso(kg): ', size=(0, 1)), sg.Input(size=(15,0),key='peso')],
            [sg.Text('Informe a sua altura(cm):', size=(0, 1)), sg.Input(size=(15,0),key='altura')],
            [sg.Button('Calcular'), sg.Button('Sair')],
            [sg.Output(size=(80, 13))]

        ]

        self.janela = sg.Window('I   M   C').Layout(layout)


    def Iniciar(self):
        while True:
            self.button, self.valores = self.janela.read()
            if self.button == 'Sair' or self.button == sg.WIN_CLOSED:
                break
            peso = float(self.valores['peso'])
            altura = float(self.valores['altura'])
            caluloImc = peso / (altura * altura)
            if caluloImc <= 18.5:
                print(f'Seu IMC esta em: {caluloImc:.2f} a Classificação esta em: MAGREZA')
                Linha()
            elif caluloImc > 18.5 and caluloImc < 24.9:
                print(f'Seu IMC esta em: {caluloImc:.2f} a Classificação esta em: SAUDÁVEL')
                Linha()
            elif caluloImc > 25 and caluloImc < 29.9:
                print(f'Seu IMC esta em: {caluloImc:.2f} a Classificação esta em: SOBREPESO')
                Linha()
            elif caluloImc >30 and caluloImc < 34.9:
                print(f'Seu IMC esta em: {caluloImc:.2f} a Classificação esta em: OBESIDADE GRAU 1')
                Linha()
            elif caluloImc > 35 and caluloImc < 39.9:
                print(f'Seu IMC esta em: {caluloImc:.2f} a Classificação esta em: OBESIDADE SEVERA GRAU 2')
                Linha()
            elif caluloImc > 40:
                print(f'Seu IMC esta em: {caluloImc:.2f} a Classificação esta em: OBESIDADE MÓRBIDA GRAU 3')
                Linha()



def Linha():
    print('='*70)


calc = Imc()
calc.Iniciar()
