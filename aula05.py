import os 
os.system("cls")
#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#atividade1
#replace("valor1","valor2")-> Substitui o valor1 pelo valor2
# nota1= float(input("digite a primeira nota:"))
# nota2= float(input("digite a segunda nota:"))

# media=(nota1+nota2)/2
#:.2f -> formata para 2 casas decimais apenas no fstring
# print(f"Sua media é: {media:.2f}")

# if media < 5:
#     print("Reprovado")
# elif media >= 5 and media <= 7:
#     print("Em recuperção")
# elif media > 7:
#     print("Aprovado")

#reescrevendo de outra forma
# nota1= float(input("digite a primeira nota:").replace(",","."))
# nota2= float(input("digite a segunda nota:").replace(",","."))

# media=(nota1+nota2)/2
# print(f"Sua media é: {media:.2f}")

# if media < 5:
#     print("Reprovado")
# elif media >= 5 and media <= 7:
#     print("Em recuperção")
# else:
#     print("Aprovado")

#atividade2

# peso=float(input("Digite seu peso: ").replace(",","."))
# altura=float(input("Digite sua altura: ").replace(",","."))
# imc=peso/(altura*altura)

# print(f"Seu imc é:{imc:.2f}")

# if imc<17:
#     print("Muito abaixo do peso")
# elif imc>=17 and imc<=18.49:
#     print("Abaixo do peso")
# elif imc>=18.5 and imc<=24.99:
#     print("Peso normal")
# elif imc>=25 and imc<=29.99:
#     print("Acima do peso")
# elif imc>=30 and imc<=34.99:
#     print("Obesidade I")
# elif imc>=35 and imc<=39.99:
#     print("Obesidade II")
# else:
#     print("Obesidade III(mórbida)")

# reescrevndo de outra maneira:
# peso=float(input("Digite seu peso: ").replace(",","."))
# altura=float(input("Digite sua altura: ").replace(",","."))
# imc=round(peso/(altura*altura),2)

# print(f"Seu imc é:{imc}")

# if imc<17:
#     print("Muito abaixo do peso")
# elif imc<=18.49:
#     print("Abaixo do peso")
# elif imc<=24.99:
#     print("Peso normal")
# elif imc<=29.99:
#     print("Acima do peso")
# elif imc<=34.99:
#     print("Obesidade I")
# elif imc<=39.99:
#     print("Obesidade II")
# else:
#     print("Obesidade III(mórbida)")

# #raw string
# print("."*15,"REAJUSTE AUTOCAR","."*15)
# print(r"""               ,.,_,.                  
#            ,.''     \                 
#           '          '                
#         /'           |                
#       /_-            |                
#     .'__      _-_    :                
#    /__        _-_    :                
#   ,_,._     ,_,._~   |___             
# .'-_ '.'.-.'-_ '.'._-^_  '.           
# |  -_ |.| |  -_ | | / |               
#  ',_,' /  _',_,'_'  /|/               
#   .  .|    ',. ._-^  |'               
#    ' '.   .'  '.    '/|               
#  ,'    '''    __'.  \/ -_             
# '_=-..--..--'^  '', : \. '.           
#      ',    .  ,   ,' \/ |  |-_        
#      / ',.. '. '. ,../  |  |  '-_     
#    ,'  . \'.:.''''    .''. '.    \.   
#  ,'    | |\       ,../   |  |      ', 
#  |     ' ''.,.''''       ', ',       |

# """)
# print("."*50)
# print("\nTABELA DE REAJUSTE DE SALÁRIO:")
# print("Salários até R$ 2799,99 :aumento de 20%;")
# print("Salários entre R$ 2800,00 e R$ 6999,99: aumento de 15%;")
# print("Salários entre R$ 7000,00 e R$ 14999,99: aumento de 10%;")
# print("Salários de R$ 15000,00 em diante: aumento de 5%")

# salario=float(input("\nDigite seu salário R$:"))

# if salario <=2799.99:
#     aumento=salario*0.20
#     total=aumento+salario
#     print(f"Salário sem reajuste R$: {salario}")
#     print("Percentual da sua faixa 20%")
#     print(f"Aumento de R$:{aumento}")
#     print(f"Novo salário R$:{total}")
# elif salario >=2800 and salario <=6999.99:
#     aumento=salario*0.15
#     total=aumento+salario
#     print(f"Salário sem reajuste R$: {salario}")
#     print("Percentual da sua faixa 15%")
#     print(f"Aumento de R$:{aumento}")
#     print(f"Novo salário R$:{total}")
# elif salario >=7000 and salario <=14999.99:
#     aumento=salario*0.10
#     total=aumento+salario
#     print(f"Salário sem reajuste R$: {salario}")
#     print("Percentual da sua faixa 10%")
#     print(f"Aumento de R$:{aumento}")
#     print(f"Novo salário R$:{total}")
# else: 
#     aumento=salario*0.05
#     total=aumento+salario
#     print(f"Salário sem reajuste R$: {salario}")
#     print("Percentual da sua faixa 5%")
#     print(f"Aumento de R$:{aumento}")
#     print(f"Novo salário R$:{total}")




















































































































































































