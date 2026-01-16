def calcula_precofinal(valor_produto,porcentagem_desconto):
    desconto = valor_produto * (porcentagem_desconto / 100)
    preco_final = valor_produto - desconto
    return preco_final

valor = float(input("Digite o valor do produto:"))
porcentagem = float(input("Digite a porcentagem de desconto (%):"))
preco_final = calcula_precofinal(valor,porcentagem)
    
print(f"O preço final com desconto é : R$ {preco_final:.2f}")