produtos = []

fim = ""

while fim != "fim":
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade de produtos: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

    fim = input("Digite Fim para encerrar ou Enter para continuar: ").lower()

print("Produtos cadastrados:")
for produto in produtos:
    print("Produto:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print()