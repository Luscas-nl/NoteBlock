from random import randint

palavraSecreta = ['BOMBA', 'PYTHON', 'IFAL', 'ONIBUS', "GALDINO", "YPISSILON"]
palavraTracinho = []
chutes = list()
numIndice = randint(0, 5)

def VerificarLetra(letra):
    posicao = 0
    if letra in chutes:
        print(f"A letra {letra} ja foi chutada")
    else:
        chutes.append(letra)
        if letra in palavraSecreta[numIndice]:
            for i in palavraSecreta[numIndice]:
                if letra == i:
                    palavraTracinho[posicao] = chute
                posicao += 1
        else:
            print(f"Não existe a letra {letra} na palavra")

for i in palavraSecreta[numIndice]:
    palavraTracinho.append('_')

while True:
    print(' ')
    print("Palavra Secreta:", end=" ")
    for i in palavraTracinho:
        print(f'{i}', end=' ')
        
    chute = str(input("\nDigite uma letra: ").upper())
    VerificarLetra(chute)
    
    if("_" not in palavraTracinho):
        break
    
print(" ")
print("Você finalizou a palavra")
print(f"Palavra Secreta: {palavraSecreta[numIndice]}")
print(f"Quantidade de chutes: {len(chutes)}")