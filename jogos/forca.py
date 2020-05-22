import random


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def palavra_sorteada():
    with open("palavras.txt", "r") as arquivo:
        palavras = [palavra.strip() for palavra in arquivo]
        palavra_secreta = random.choice(palavras).upper()
    return palavra_secreta


def inicia_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ").strip().upper()
    return chute


def chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def mensagem_resultado(resultado):
    if resultado:
        print("Você ganhou!")
    else:
        print("Você perdeu!")


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = palavra_sorteada()
    letras_acertadas = inicia_letras_acertadas(palavra_secreta)
    erros = 0
    print(letras_acertadas)
    print("Dica: A palavra possui {} letras.".format(len(palavra_secreta)))

    while True:
        chute = pede_chute()
        if chute in palavra_secreta:
            chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print("Restam {} tentativas".format(len(palavra_secreta)-erros))
        print(letras_acertadas)
        if erros == 6:
            mensagem_resultado(False)
            break
        if "_" not in letras_acertadas:
            mensagem_resultado(True)
            break


if __name__ == "__main__":
    jogar()
