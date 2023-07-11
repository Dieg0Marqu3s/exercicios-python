# Conceito de armstrong: é um número de n dígitos que é igual a soma de cada um dos seus dígitos elevado a n-ésima potência .
# Critérios:
# O número deve ser um inteiro positivo. Números negativos, frações ou números decimais não são considerados números de Armstrong.
# O número deve ser expresso na base decimal. Números em outras bases, como binário ou hexadecimal
# A soma dos dígitos elevados à potência do número total de dígitos deve ser igual ao próprio número

numero = int(input("Digite um número: "))
numero_str = str(numero)
soma = 0

numero_digitos = len(numero_str) # len Retorna o número de itens em um conteiner

for digito in numero_str:
    soma += int(digito) ** numero_digitos

if soma == numero:
    print(numero, "é um número de Armstrong.")
else:
    print(numero, "não é um número de Armstrong.")