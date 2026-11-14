import random

numero_secreto = random.randint(5, 50)
max_tentativas = 3

print("Jogo do Número Secreto")
print("Tente adivinhar um número entre 5 e 50.")

for tentativa in range(1, max_tentativas + 1):
    try:
        palpite = int(input(f"Tentativa {tentativa}/{max_tentativas}: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite > numero_secreto:
        print("Tente um número menor.")
    else:
        print("Tente um número maior.")
else:
    print(f"Suas tentativas acabaram. O número era {numero_secreto}.")
