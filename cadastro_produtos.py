#Programa de Cadastro, consulta e remoção de produtos

listaProdutos = []


def cadastrarProduto(produto): #Função para cadastrar produto
    print("O código do produto a ser cadastrado é {}".format(produto))
    nome = input("Digite o nome do produto: ")
    fabricante = input("Digite o nome do fabricante do produto: ")
    valor = input("Digite o valor do produto")

    dict_produto = {"codigo":produto,"nome":nome,"fabricante":fabricante, "valor": valor}

    listaProdutos.append(dict_produto.copy())

def consultarProduto(): #Função para consultar produto
    while True:
        try:
            print("1) Consultar todos os produtos")
            print("2) Consultar produtos por código")
            print("3) Consultar produtos por fabricante")
            print("4) Retornar")
            consulta = int(input("Digite a opção que deseja: "))

            if consulta == 1:
                print("Você está consultando todos os produtos: ")
                for produtos in listaProdutos:
                    for key, value in produtos.items():
                        print("{}:{}".format(key,value))
            elif consulta == 2:
                print("Você está consultando o produto pelo seu código: ")
                entrada = int(input("Digite o código do produto: "))
                for produtos in listaProdutos:
                    if produtos["codigo"] == entrada:
                        for key, value in produtos.items():
                            print("{}:{}".format(key, value))
            elif consulta == 3:
                print("Você está consultando o produto pelo seu fabricante: ")
                entrada = input("Digite o fabricante do produto: ")
                for produtos in listaProdutos:
                    if (produtos["fabricante"] == entrada):
                        for key, value in produtos.items():
                            print("{}:{}".format(key, value))
            elif consulta == 4:
                return
            else:
                print("Digite um número válido!")

        except ValueError:
            print("Digite um valor válido!")

def removerProduto(): #Função para remover produto
    print("Você está removendo um produto: ")
    entrada = int(input("Digite o código do produto: "))
    for produtos in listaProdutos:
        if (produtos["codigo"] == entrada):
                listaProdutos.remove(produtos)
                print("Produto número: ", entrada, "removido")


#Menu principal
print("Bem-vindo(a) ao cadastro e consulta de produtos do Teteu!") #Identificação Pessoal

codigo_produto = 0 #Contador para o código

while True:
    try:
        print("1 - Cadastrar produto")
        print("2 - Consultar produto")
        print("3 - Remover produto")
        print("4 - Sair")
        opcao = int(input("Escolha a opção que deseja: "))

        if opcao == 1:
            codigo_produto = codigo_produto + 1
            cadastrarProduto(codigo_produto)
        elif opcao == 2:
            consultarProduto()
        elif opcao == 3:
            removerProduto()
        elif opcao == 4:
            print("Até a próxima!")
            break
        else:
            print("Digite uma opção válida!")
            continue
    except ValueError:
        print("Digite um valor válido!")
        continue
