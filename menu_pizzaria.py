
#Programa de escolha de menu de pizzaria do Matheus Felipe

print("***** Bem-vindo(a) a pizzaria do Teteu! *****")

#Dicionários para salvar os valores referentes aos códigos e as pizzas

pizzas = {21:"Napolitana", 22:"Margherita", 23:"Calabresa",24:"Toscana",25:"Portuguesa"}

valores_media = {21:20.00, 22: 20.00, 23:25.00, 24:30.00, 25:30.00}
valores_grande = {21:26.00, 22: 26.00, 23:32.50, 24:39.00, 25:39.00}
valor = 0


#Menu de interação do usuário
print("--------------------- Cardápio ---------------------")
print("| Código | Descrição  | Pizza Média | Pizza Grande |")
print("|   21   | Napolitana |    R$ 20,00 |    R$ 26,00  |")
print("|   22   | Margherita |    R$ 20,00 |    R$ 26,00  |")
print("|   23   | Calabresa  |    R$ 25,00 |    R$ 32,50  |")
print("|   24   | Toscana    |    R$ 30,00 |    R$ 39,00  |")
print("|   25   | Portuguesa |    R$ 30,00 |    R$ 39,00  |")

#Parte lógica para cálculo dos valores e escolha dos sabores
while(True):

 tamanho = input("Digite o tamanho da pizza desejada(M/G): ")
 if (tamanho.lower() != "g" and tamanho.lower() != "m"):
  print("Digite um tamanho válido!")
  continue

 codigo = int(input("Digite o código do sabor desejado: "))
 if (codigo != 21 and codigo != 22 and codigo != 23 and codigo != 24 and codigo != 25):
  print("Digite um código válido!")
  continue

 if (tamanho.lower() == "m"):
  valor = valor + valores_media[codigo]
 else:
  valor = valor + valores_grande[codigo]



 print("Pizza {}, tamanho: {}, adicionada ao carrinho!".format(pizzas[codigo],tamanho))



 confirma = input("Deseja finalizar o carrinho e prosseguir para o pagamento?: (S/N)")
 if confirma.lower() == "s":
  break

#Finalização
print("O total a ser pago é R${}".format(valor))




