# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


produto = input("digite o nome do produto:")
preco = float(input("digite o preço do produto"))
porcentagem = float(input("digite a porcentagem de desconto:"))

desconto = preco * (porcentagem / 100)
valor_final = preco - desconto

print("produto:", produto)
print("valor do desconto:", desconto)
print("valor_final:", valor_final)

