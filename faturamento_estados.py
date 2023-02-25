SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

faturamento_total = (SP + RJ + MG + ES + Outros)


porcentagem_sp = ((SP / faturamento_total) * 100)
porcentagem_rj = ((RJ / faturamento_total) * 100)
porcentagem_mg = ((MG / faturamento_total) * 100)
porcentagem_es = ((ES / faturamento_total) * 100)
porcentagem_outros = ((Outros / faturamento_total) * 100)


print (f'O faturamento do estado de São Paulo representa {porcentagem_sp:.2f}% do faturamento total.')
print (f'O faturamento do estado de Rio de Janeiro representa {porcentagem_rj:.2f}% do faturamento total.')
print (f'O faturamento do estado de Minas Gerais representa {porcentagem_mg:.2f}% do faturamento total.')
print (f'O faturamento do estado de Espirito SantoS representa {porcentagem_es:.2f}% do faturamento total.')
print (f'O faturamento de outros estados representa {porcentagem_outros:.2f}% do faturamento total.')


