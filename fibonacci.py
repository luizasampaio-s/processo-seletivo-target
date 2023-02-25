# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# Armazenando os dois primeiros números da sequência em uma lista;
fibonacci_list = [0,1]

# Pedindo uma entrada para o usuário
entrada_valor = int(input('Digite um número: '))

# Laço de repetição que realizará o seguinte teste lógico:
### Enquanto o último número da lista for menor que o valor da entrada,
### adicione ao final da lista a soma dos dois ultimos válores
while fibonacci_list[-1] < entrada_valor:
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])


# Estrutura condicional que fará o seguinte teste lógico:
## Se o valor da entrada fizer parte da sequência fibonacci, mostre no terminal: 'O numero {entrada_valor} faz parte da sequencia fibonacci'
## Se o valor da entrada não fizer parte da sequência fibonacci, mostre no terminal: 'O numero {entrada_valor} não faz parte da sequencia fibonacci
if entrada_valor in fibonacci_list:
    print(f'O numero {entrada_valor} faz parte da sequencia fibonacci')
else:
    print(f'O numero {entrada_valor} não faz parte da sequencia fibonacci')





