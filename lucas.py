import random

numero_secreto = random.randint(5, 50)

palpite = int(input("Tente adivinhar o número:  "))

if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
elif palpite > numero_secreto:
    print("Tente um número menor.")
else:
    print("Tente um número maior")
tentativas = 3
max_tentativas = 3

while tentativas < max_tentativas:
    #...(código do palpite e verificação vai aqui)
tentativas = 3

print(f"Fim do jogo. O número era {numero_secreto}.")