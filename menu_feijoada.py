
#Programa de Feijoada por Volume do Matheus Felipe


#Declaração de variáveis e dicionários para uso e facilitação futura caso algum valor for ser modificado.
opcao_feijoada = {"b": 1.00, "p":1.25, "s":1.50}
acompanhamentos = {1:"200gr de Arroz", 2:"150gr de farofa especial", 3:"100gr de couve cozida",4:"1 Laranja Descascada"}
valor_acompanhamento = { 1:5, 2:6, 3:7, 4:3}
custo = 0
volume = 0
opcao = 0
acompanhamento = 0
valor = 0
total_acompanhamento = 0

#Tela de boas vindas
print("***** Seja bem-vindo(a) a feijoada do Teteu! *****")
print("Pedidos de 300ml até 5l !")

#Função para requisição do volume da feijoada
def volumeFeijoada():
    global volume
    while(True):
        try:
            volume = int(input("Qual a quantidade de feijoada desejada? (ml)"))
            if (volume < 300):
                print("Só aceitamos pedidos maiores que 300ml, tente novamente.")
                continue
            elif(volume > 5000):
                print("Só aceitamos pedidos menores que  5l, tente novamente.")
                continue
            else:
                break
        except ValueError:
            print("Digite um número válido")

#Função para requisição da opção da qualidade da feijoada
def opcaoFeijoada():
    global opcao
    while(True):

        print("| B | - Básica (Feijão + Paiol + Costelinha( X 1.00 )")
        print("| P | - Premium (Feijão + Paiol + Costelinha + Partes de Porco( X 1.25 )")
        print("| S | - Suprema (Feijão + Paiol + Costelinha + Partes de Porco + Charque + Calabresa + Bacon( X 1.50 )")
        opcao = (input("Entre com a opção da feijoada: "))


        if (opcao.lower() != "b" and opcao.lower() != "p" and opcao.lower != "s"):
            print("Digite uma opção válida!")
            continue

        else:
            break

#Função para adição dos acompanhamentos e cálculo do valor dos acompanhamentos
def acompanhamentoFeijoada():
    global opcao
    global volume
    global valor
    global acompanhament
    global acompanhamentos
    global opcao_feijoada
    global valor_acompanhamento
    global total_acompanhamento

    while(True):
        try:
            print("Deseja mais algum acompanhamento?")
            print("0 - Não desejo mais acompanhamentos")
            print("1 -", acompanhamentos[1], "R$", valor_acompanhamento[1])
            print("2 -", acompanhamentos[2], "R$", valor_acompanhamento[2])
            print("3 -", acompanhamentos[3], "R$", valor_acompanhamento[3])
            print("4 -", acompanhamentos[4], "R$", valor_acompanhamento[4])

            acompanhamento = int(input(">>>"))
            if (acompanhamento == 0):
                break
            elif (acompanhamento != 1 and acompanhamento != 2 and acompanhamento != 3 and acompanhamento != 4):
                print("Digite uma opção válida!")
                continue


            print(acompanhamentos[acompanhamento], "adicionado a feijoada!")
            total_acompanhamento = total_acompanhamento + valor_acompanhamento[acompanhamento]
        except ValueError:
            print("Digite um número válido!")



#Execução das funções
volumeFeijoada()
opcaoFeijoada()
acompanhamentoFeijoada()

#Finalização com cálculo e retorno do total para o cliente
valor = (volume*opcao_feijoada[opcao])

print("Sua feijoada está com o valor de R${}".format(valor))
print("Seus acompanhamentos ficaram em R${}".format(total_acompanhamento))
print("O total da sua conta ficou em R${}".format(valor + total_acompanhamento))