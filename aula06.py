import os 
os.system("cls")
#Estruturas condicionais IF ELSE (ELIF)
#SWITCH CASE -> (match case) escolha caso (a partir da versão 3.10)
#match valor: 
# #caso valor

# linguagem = 100

# match linguagem:
#     case "python":
#         print("é facil")
#     case "java":
#         print("muito código, python faz com linhas menores")
#     case "c#":
#         print("massa")
#     case "js":
#         print("sou do back")
#     case "html":
#         print("snow ball não cala a boca")
#     case 10:
#         print("entrou aqui")
#     case _:
#         print("outro caso")

# print("1-segunda")
# print("2-terça")
# print("3-quarta")
# print("4-quinta")
# print("5-sexta")
# print("6-sábado")
# print("7-domingo")
# dsemana=int(input("digite um dia da semana:"))
# match dsemana :
#     case 1:
#         print("segunda")
#     case 2:
#         print("terça")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         print("sábado")
#     case 7:
#         print("domingo")
#     case _:
#         print("você não digitou um número de 1 a 7")

# print("*"*15,"loja de celular","*"*15)
# print(r"""
# 1-Iphone 15 - R$:5000,00
# 2-Xiomi Redmi 13 PRO PLUS 512GB - R$:2500,00
# 3-Sansung S25 265 GB - R$: 6999,99
# Frete: SP->10,00
#         MG->15,00
#         RS->20,00
# """)
# celular=int(input("Digite o nº do produto:"))
# estado=input("Digite a sigla do estado:").upper()
# print("*"*50)

# preco=0
# frete=0
# match celular :
#     case 1:
#         preco=5000
#     case 1:
#         preco=2500
#     case 2:
#         preco=6999.99

# match estado :
#     case "SP":
#         frete=10
#     case "MG":
#         frete=15
#     case "RS":
#         frete=20

# print(f"Preço R$:{preco:.2f}")
# print(f"Frete R$:{frete:.2f}")
# print(f"Total R$:{preco + frete:.2f}")

#outra forma de resolver

# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valortotal:.2f}")

import random

# valor = 0
#randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")


# Desenhos pedra papel tesoura

# print("JOGO PEDRA PAPEL TESOURA")

# papel = """
# PAPEL
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """
# PEDRA
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """
# TESOURA
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """

# jogador = input("Escolha entre pedra, papel ou tesoura: ")
# match jogador:
#     case "pedra":
#         jogador=pedra
#     case "tesoura": 
#         jogador =tesoura
#     case "papel":
#         jogador = papel

# #1-> pedra , 2-> papel , 3->tesoura

# maquina = random.randint(1,3)

# match maquina:
#     case 1:
#         maquina=pedra
#     case 2: 
#         maquina =papel
#     case 3:
#         maquina =tesoura


# print(f"voce escolheu  {jogador}")
# print(f"maquina escolheu {maquina}")

# match jogador:
#     case _ if jogador == maquina:
#         print("empate")
#     case _ if jogador==pedra and maquina ==tesoura:
#         print("Voce ganhou")
#     case _ if jogador == tesoura and maquina ==papel:
#         print("Voce ganhou")
#     case _ if jogador == papel and maquina ==pedra:
#         print("voce ganhou")
#     case _ :
#         print("voce perdeu")


# print("2 MODO - PEDRA PAPEL TESOURA")


print("JOGO PEDRA PAPEL TESOURA ")

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


tesoura = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

#pedra=1 papel=2 tesoura=3
mao = input("Digite pedra ou papel ou tesoura :")
maquina = random.randint(1,3)

match maquina :
    case 1:
        maquina = "pedra"
    case 2:
        maquina = "papel"
    case 3 :
        maquina ="tesoura"

match mao:

    case _ if mao== "pedra" and maquina=="pedra" :
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {pedra}")
        print("EMPATOU!")
    
    case _ if mao== "pedra" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {pedra}")
        print("PERDEU!")
    case _ if mao== "pedra" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {pedra}")
        print("GANHOU!")
    case _ if mao== "papel" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {papel}")
        print("EMPATOU!")
    case _ if mao== "papel" and maquina=="pedra":
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {papel}")
        print("GANHOU")
    case _ if mao== "papel" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {papel}")
        print("PERDEU!")
    case _ if mao== "tesoura" and maquina=="pedra":
        print(f"Maquina: {maquina} {pedra}")
        print(f"Você: {mao}  {tesoura}")
        print("PERDEU!")
    case _ if mao== "tesoura" and maquina=="papel":
        print(f"Maquina: {maquina} {papel}")
        print(f"Você: {mao}  {tesoura}")
        print("GANHOU!")
    case _ if mao== "tesoura" and maquina=="tesoura":
        print(f"Maquina: {maquina} {tesoura}")
        print(f"Você: {mao}  {tesoura}")
        print("EMPATOU!")
    case _:
        print("DIGITOU ERRADO! ESCOLHA PAPEL OU TESOURA OU PEDRA")