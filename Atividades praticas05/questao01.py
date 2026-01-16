def calcula_gorjeta(valor_conta,porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = float(input("Digite o valor da conta:"))
porcentagem = float(input("Digite a porcentagem da gorjeta:"))
valor_gorjeta = calcula_gorjeta(valor,porcentagem)
    
print(f"O valor da gorjeta é: R$ {valor_gorjeta:.2f}")