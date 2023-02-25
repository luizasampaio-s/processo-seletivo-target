# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve
# dentro do valor total mensal da distribuidora.

# Armazenando os valores dos faturamentos em variáveis 
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

# Somando os valores de cada estado para obter o faturamento total
faturamento_total = (SP + RJ + MG + ES + Outros)

# Realizando calculo simples de porcentagem
porcentagem_sp = ((SP / faturamento_total) * 100)
porcentagem_rj = ((RJ / faturamento_total) * 100)
porcentagem_mg = ((MG / faturamento_total) * 100)
porcentagem_es = ((ES / faturamento_total) * 100)
porcentagem_outros = ((Outros / faturamento_total) * 100)

# Print para exibir os valores de modo formatado no terminal
print (f'O faturamento do estado de São Paulo representa {porcentagem_sp:.2f}% do faturamento total.')
print (f'O faturamento do estado de Rio de Janeiro representa {porcentagem_rj:.2f}% do faturamento total.')
print (f'O faturamento do estado de Minas Gerais representa {porcentagem_mg:.2f}% do faturamento total.')
print (f'O faturamento do estado de Espirito SantoS representa {porcentagem_es:.2f}% do faturamento total.')
print (f'O faturamento de outros estados representa {porcentagem_outros:.2f}% do faturamento total.')


