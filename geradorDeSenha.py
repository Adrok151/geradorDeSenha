import random

def gerarSenha():
    caracteres = [
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ,'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' ,'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z'],
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['!', '@', '#', '$', '%', '&', '*', '/', '(', ')', '?']
        ]
    senha = []

    for contador in range(33):
        linha = random.randrange(4)
        coluna = random.randrange(len(caracteres[linha]))
        senha.extend(caracteres[linha][coluna])
        print(senha[contador], end='')

gerarSenha()