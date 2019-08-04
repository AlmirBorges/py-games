import random

def jogar():

    if (__name__ == "__main__"):
        jogar()

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = (random.randrange(1, 101))

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20
    elif (nivel==2):
        tentativas = 10
    elif (nivel==3):
        tentativas = 5

    pontos = 1000

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute = input("Tente acertar o número secreto:")
        print("Você digitou", chute, sep=" ", end="\n\n")
        chute = int(chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!", end="\n\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto


        if (acertou):
            print("Você acertou o número secreto e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("O número digitado é maior que o número secreto.", end="\n")
            elif(menor):
                print("O número digitado é menor que o número secreto.", end="\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Game over")