numeros = []
entrada = input("Digite um número ou escreva 'Sair' para terminar: ")
while entrada != "Sair":
    numero =float(entrada)
    numeros.append(numero)
    entrada = input("Digite um número ou 'Sair' para terminar: " )
if len(numeros) > 0:
    media = sum(numeros) /len(numeros)
    print(f"A média dos números é {media:.2f}")
else:
    print("Nenhum número foi inserido")