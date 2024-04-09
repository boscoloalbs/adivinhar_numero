import random

def adivinhar(numero_aleatorio):
    i = 0
    while True:
        numero_adivinhe = int(input("Tente adivinhar o número! Digite um número de 0 a 100: "))
        print(f"\n\nO número é: {numero_aleatorio}!\n")
        if numero_adivinhe < numero_aleatorio:
            i += 1
            print("Número incorreto! O número informado é menor do que o número a ser adivinhado!")
            print(f"Você já fez {i} tentativas!\n")
        elif numero_adivinhe > numero_aleatorio:
            i += 1
            print("Número incorreto! O número informado é maior do que o número a ser adivinhado!")
            print(f"Você já fez {i} tentativas!\n")
        else:
            i += 1
            print(f"\nParabéns!! Você acertou o número com um total de {i} tentativas!!\n") 
            break 

numero_aleatorio = random.randint(0,100)

print("\n...Gerando número aleatório...\n")
numero_adivinhe = adivinhar(numero_aleatorio)
