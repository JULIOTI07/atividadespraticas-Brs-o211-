notas = []

while True:
    try:
        entrada = input("Digite uma nota entre 0 e 10 (ou 'fim' para encerrar):")

        if entrada.lower() == 'fim':
            break

        nota = float(entrada)

        if nota < 0 or nota > 10:
            raise Exception("Nota inválida. Deve estar entre 0 e 10")
        notas.append(nota)
        
    except ValueError:
        print("Você deve digitar apenas notas")
    except Exception:
        print("Nota inválida")

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas) if len(notas) > 0 else 0
print(f"A média final: {media:.2f}")