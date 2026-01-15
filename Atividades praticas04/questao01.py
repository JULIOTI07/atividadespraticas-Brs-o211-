def calculadora_simples():        
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Escolha a operação (+, -, *, /): ")

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                print("Erro: Operação inválida.")
                continue  

            print(f"Resultado: {resultado}")
            break  

        except ValueError:
            print("Erro: Digite apenas números válidos.")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")

calculadora_simples()

