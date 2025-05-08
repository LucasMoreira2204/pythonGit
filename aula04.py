import os
os.system ("cls")
#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")

# nome = "teste"
# if "teste" == nome:
#     print(1)
# else:
#     print(2)

# Exercicios - if Else

#desafio

# idade=int(input("digite sua idade: "))

# if idade >= 18 and idade <120:
#     print("Maior de idade")
# else:
#     if idade <18 and idade > 0:
#         print("Menor de idade")
#     else:
#         print("idade invalida")

#outro jeito        
# idade=int(input("digite sua idade: "))

# if idade < 0 or idade >120:
#     print("idade invalida")
# else:
#     if idade >=18:
#         print("Maior de idade")
#     else:
#         print("Menor de idade")

# email=input("digite o email: ")
# senha=input("digite a senha: ")

# if email ==  "python@senai.com" and senha == "12345678":
#     print("Usuário autenticado")
# else:
#     os.system("color 4")
#     print("Usuário ou senha Inválidos")

#atividade4

# print("*"*15,"Iphone de ultima geraçao","*"*15)
# print("R$: 0.30 -> menos que uma dúzia")
# print("R$: 0.25 -> pelo menos doze") 
# print("\n")
# qnt=int(input("Digite a quantidade de maças que deseja levar: "))

# if qnt <12:
#     valor= qnt*0.30
#     print(f"{qnt} maças você ira pagar R$0.30 unidade ", "R$:",valor )
# else:
#     valor= qnt*0.25
#     print(f"{qnt} maças você ira pagar R$0.25 unidade ", "R$:",valor )

#atividade1
# l=input("digite uma letra:")

# if l == "a" or l =="e" or l =="i" or l =="o" or l =="u" or l == "A" or l =="E" or l =="I" or l =="O" or l =="U":
#     print("essa letra é uma vogal!")
# else:
#     print("essa letra é uma consoante!")

#reescrevendo de outra maneira
#upper() -> CONEVRTER TUDO PARA MAIUSCULO
#lower() -> converter tudo para minusculo
# l=input("digite uma letra:").lower()

# if  l == "a" or l =="e" or l =="i" or l =="o" or l =="u":
#     print("essa letra é uma vogal!")
# else:
#     print("essa letra é uma consoante!")

#reescrevendo de outra maneira
#AND OR in
# l=input("digite uma letra:")

# if l in "aeiouAEIOU":
#     print("essa letra é uma vogal!")
# else:
#     print("essa letra é uma consoante!")

#atividade2
# n1=float(input("digite um numero:"))
# n2=float(input("digite outro numero:"))

# if n1 > n2:
#     print(f"Numero maior:{n1}")
#     print(f"Numero menor:{n2}")
# else:
#     print(f"Numero maior:{n2}")
#     print(f"Numero menor:{n1}")





































