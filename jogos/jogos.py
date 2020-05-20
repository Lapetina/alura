import forca
import adivinhacao_for

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        forca.jogar()
        print("Jogando forca")
    elif jogo == 2:
        adivinhacao_for.jogar()
        print("Jogando adivinhação")


if __name__ == "__main__":
    escolhe_jogo()
