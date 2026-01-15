pares = 0 
impares = 0

while True:
   try: 
    entrada = input("Digite um número ou fim para sair:")

    if entrada.lower() == 'fim':
        break

    numero = int(entrada)

    if numero % 2 == 0:
        print(f"{numero} é par")
        pares += 1

    else:
        print(f"{numero} é impar")
        impares += 1
   
   except ValueError:
      print("Erro: Digite apenas números ou 'fim' para sair")

print("\n--- Resultado Final ---")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")      


