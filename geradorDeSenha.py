import random
import tkinter

def gerarSenha(texto):
    caracteres = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ,'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['!', '@', '#', '$', '%', '&', '*', '/', '(', ')', '?', '<', '>', '^']
        ]
    Lista = []

    for contador in range(32):
        linha = random.randrange(4)
        coluna = random.randrange(len(caracteres[linha]))
        Lista.extend(caracteres[linha][coluna])

    senha = ''.join(Lista) + '\n'
    texto.insert(tkinter.END, senha)

def limparQuadro(texto):
    texto.delete(1.0, tkinter.END)

def iniciarGerador():
    janela = tkinter.Tk()
    janela.title('Gerador de Senha')

    texto = tkinter.Text(janela)
    texto.grid(row=1, column=0)

    quadro = tkinter.Frame(janela, relief=tkinter.RAISED, bd=2)
    botaoLimpar = tkinter.Button(quadro, text='Limpar', command=lambda: limparQuadro(texto))
    botaoSenha = tkinter.Button(quadro, text='Gerar Senha', command=lambda: gerarSenha(texto))

    botaoLimpar.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
    botaoSenha.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    quadro.grid(row=0, column=0, sticky='ew')
    
    janela.mainloop()

iniciarGerador()