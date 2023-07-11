# teste_string = "Teste"
# teste_number = 10
# teste_numero_inteiro = 1.0
# boleano_true = True
# boleano_false = False
 
# print(teste_number)
# print (type(teste_number))

# print(teste_string)
# print (type(teste_string))

# print(teste_numero_inteiro)
# print (type(teste_numero_inteiro))

# print(boleano_true)
# print (type(boleano_true))

# print(boleano_false)
# print (type(boleano_false))

# teste_upper = "testando 123"
# print(teste_upper.upper())

# teste_title = "autoban, crr, tebe, ecovias"
# print(teste_title.title())

# print("--------------------------------")

# nome = "Diego"
# data_de_aniversario = "23/04/2002"
# frase = f"Meu nome é: {nome} e a minha data de aniversário é: {data_de_aniversario}"
# print(frase)

# valor1 = 10
# valor2 = 100

# soma = valor1 + valor2
# print(f"Soma: {soma}")

# subtracao = valor1 - valor2
# print(f"Subtração: {subtracao}")

# multiplicacao = valor1 * valor2
# print(f"Multiplicação: {multiplicacao}")

# divisao = valor1 / valor2
# print(f"Divisão: {divisao}")

# divisao_inteira = valor1 % valor2
# print(f"Divisão inteira: {divisao_inteira}")

# Criar uma váriavel que calcula o IMC baseado nas variaveis: peso, altura e imc if imc < 1,8: print(" ")
# input("Digite seu peso: ")

print("                                ") # Coloca espaço para melhorar a visualização

# Solicita o valor peso
peso = input("Digite seu peso:")
peso_numeral = float(peso)

# Solicita o valor Estatura
estatura = input("Digite sua estatura:")
estatura_numeral = float(estatura)

# Calcula o IMC
imc = peso_numeral / estatura_numeral **2  

# Condições
if imc < 18.5:
    print(f"Seu IMC é: {imc}. Você está abaixo do peso ideal para o seu IMC")

elif imc > 25:
    print(f"Seu IMC é: {imc}. Você está acima do peso ideal para o seu IMC")

else: print(f"Seu IMC é: {imc}. Você está com o peso ideal")

print("                                ") # Coloca espaço para melhorar a visualização
print("--------------------------------") # Coloca uma linha para melhorar a visualização

