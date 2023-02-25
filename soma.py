
# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# int INDICE = 13, SOMA = 0, K = 0;

# enquanto K < INDICE faça
# {
# K = K + 1;
# SOMA = SOMA + K;
# }

# imprimir(SOMA);

# Armazenando valores dentro de variáveis
indice = 13
soma = 0
k = 0

# Laço de repetição que fara o seguinte teste lógico:
## Enquanto o valor da variável k for menor que indice, soma +1 no valor da variável k e +1 na variável soma.
while k < indice:
  k = k+1
  soma = soma + k

print (soma)