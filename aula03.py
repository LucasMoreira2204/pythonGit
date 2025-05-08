import os
os.system("cls")

#Continuação Input com Int e Float
#int() -> converte para inteiro
#float() -> converte para nao quebrado

# exemplo1
# numero = 10
# numero2 = input("Digite um numero: ")
# print("o tipo de numero é",type(numero2))
# soma = numero + int(numero2)
# print("soma de:" ,{numero} , "+" , "15" , "=" , soma)

# exemplo2
# num1 = input("digite um numero: ")
# soma = float(num1) + 15
# print("A Soma de ",num1 , "+", "15" ,"=", soma)

# exemplo3
# n1 = input("digite um numero: ")
# n2 = input("digite outro numero:")

# soma = float(n1)+float(n2)

# print(f"a soma de {n1} + {n2} = ", soma)

# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero:"))

# soma = n1+n2

# print(f"a soma de {n1} + {n2} = ", soma)

#atividade1

# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))
# multiplicacao = float(n1) * (n2)
# print(f"A multiplicaçao de {n1} * {n2} =",  multiplicacao)

#atividade2

# numero = int(input("digite um numero: "))
# antecessor = numero - 1 
# sucessor = numero + 1
# print(f"O antecessor de {numero} é: ",antecessor)
# print(f"O sucessor de {numero} é: ",sucessor)

#atividade3

# n = int(input("digite seu ano de nascimento: "))
# idade = 2025 - n
# print(f"Você tem: {idade} anos")

#porcentagem
# print("25% de 100 = ", 0.25 * 100)
# print("4% de 400 = ", 0.04 * 400)
# print("99% de 1525 = ", 0.99 * 1525)

#supondo que um produto custa 150 reais
#e o caixa deu um desconto de 15%
# exemplo = float(input("digite o preco do produto: "))
# desconto = 0.15 * exemplo
# print("o preco do produto com 15% de desconto é ", exemplo-desconto)

#atividade4
# print("*"*15,"SUPERMERCADO SENAI","*"*15)

# produto1 = (input("digite o nome do primeiro produto: "))
# preco1 = float(input("digite o valor desse produto: "))

# produto2 = (input("digite o nome de um outro produto: "))
# preco2 = float(input("digite o valor desse produto: "))

# desconto1 = 0.10*preco1
# desconto2 = 0.25*preco2

# valorfinalcomdesconto1=round(preco1-desconto1,2)
# valorfinalcomdesconto2=round(preco2-desconto2,2)

# print("."*20,"CAIXA","."*20)

# print(f"{produto1} custa {preco1} com 10% = {valorfinalcomdesconto1}")
# print(f"{produto2} custa {preco2} com 10% = {valorfinalcomdesconto2}")

# print("."*20,"TOTAL","."*20)

# total =  valorfinalcomdesconto1+valorfinalcomdesconto2

# print(f"Total da compra -> R$: {total}")

#roud(valor, quantidade de casas decimais) -> faz o arredondamento dos valores