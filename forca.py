

def jogar():
    print('Bem vindo ao pycharm')
    print("********************")
    print("Jogo de Forca")
    print("********************")

    print("Fim do jogo")

    palavra_secreta = "cerveja"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input('Qual letra?').lower()
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print('Encontrei a letra {} na posicao{}'.format(letra, index))
            index = index + 1




if(__name__ == "__main__"):
    jogar()