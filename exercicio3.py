import json

# Abrindo o arquivo JSON
with open('faturamento.json', 'r') as file:
    faturamento = json.load(file)

# Inicializando as variáveis de menor e maior valor de faturamento
menor = float('inf')
maior = float('-inf')

# Calculando a soma dos valores de faturamento diário e contando o número de dias com valor superior à média
soma = 0
count = 0
for dia in faturamento:
    if dia['valor'] > maior:
        maior = dia['valor']
    if dia['valor'] < menor:
        menor = dia['valor']
    if dia['valor'] != 0:
        soma += dia['valor']
        count += 1

# Calculando a média mensal
media = soma / count

# Contando o número de dias com valor superior à média
count_superior_media = 0
for dia in faturamento:
    if dia['valor'] > media and dia['valor'] != 0:
        count_superior_media += 1

# Imprimindo os resultados
print('Menor valor de faturamento: R$ {:.2f}'.format(menor))
print('Maior valor de faturamento: R$ {:.2f}'.format(maior))
print('Número de dias com faturamento superior à média mensal: {}'.format(count_superior_media))
