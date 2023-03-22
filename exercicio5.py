# string a ser invertida
s = str(input('Digite uma string que você gostaria de inverter: '))

# variável para armazenar a string invertida
s_invertida = ""

# loop para percorrer a string de trás para frente
for i in range(len(s)-1, -1, -1):
    s_invertida += s[i]

# exibe a string invertida
print(s_invertida)
