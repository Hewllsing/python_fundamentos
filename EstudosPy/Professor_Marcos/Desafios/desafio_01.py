# Colocar o computador a gerar um numero aleatorio entre 1 e 6, dar ao utilizador 3 chances para acertar.
import random

numero_aleatorio = random.randint(1, 6)
qtd_tentativa = 0

while qtd_tentativa < 3:
    adivinhe_numero = input("Tente advinhar o numero entre 1 e 6: ")

    if adivinhe_numero == numero_aleatorio:
        print(f"O seu numero selecionado foi {adivinhe_numero} e o numero sorteado {numero_aleatorio}, parabens voce acertou!")
        break
    else:
        print(f"Não é {adivinhe_numero}. Tente novamente!")
        qtd_tentativa += 1
else: print(f"O numero sorteado foi {numero_aleatorio}. Mais sorte na proxima...")