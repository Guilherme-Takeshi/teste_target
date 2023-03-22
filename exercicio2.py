num = int(input("Digite um número inteiro: "))

# Define os primeiros valores da sequência de Fibonacci
fib1, fib2 = 0, 1

# Loop para gerar a sequência até o valor digitado pelo usuário ou até ultrapassá-lo
while fib2 < num:
    fib1 = fib2
    fib2 = fib1 + fib2

# Verifica se o número pertence à sequência de Fibonacci e exibe mensagem
if fib2 == num:
    print(num, "pertence à sequência de Fibonacci")
else:
    print(num, "não pertence à sequência de Fibonacci")
