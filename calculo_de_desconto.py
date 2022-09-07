
#Programa de cálculo de desconto do Matheus Felipe Vieira de Freitas

print("Bem-vindo(a) ao mercado do Teteu!")


#Obtenção dos dados
valor = float(input("Qual o valor do produto?: "))
quantidade = int(input("Qual a quantidade que deseja desse produto?: "))


desconto = 0
porcentagem = False

#Começo da Parte lógica de condições

if(quantidade <= 4):
     desconto = 0
     porcentagem = ("0%")
elif(quantidade >= 5 and quantidade <= 19):
    desconto = 0.03
    porcentagem = "3%"
elif(quantidade >= 20 and quantidade <= 99):
    desconto = 0.06
    porcentagem = "6%"
else:
    desconto = 0.10
    porcentagem = "10%"



#Cálculo do produto
valor = (valor * quantidade)

print("Seu carrinho tem um total de R${}".format(valor))

#Condicional caso exista desconto na compra do cliente
if (desconto != 0):
    print("Você adquiriu um desconto de: {}".format(porcentagem))
    print("O valor com desconto ficou em R${}".format(valor - (valor*desconto)))

