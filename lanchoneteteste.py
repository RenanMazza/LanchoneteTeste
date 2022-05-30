# lista de produtos
produtos = [
    [100, 'Cachorro Quente        ',  'R$  9,00',  9.00],
    [101, 'Cachorro Quente Duplo  ',  'R$ 11,00', 11.00],
    [102, 'X-Egg                  ',  'R$ 12,00', 12.00],
    [103, 'X-Salada               ',  'R$ 12,00', 12.00],
    [104, 'X-Bacon                ',  'R$ 14,00', 14.00],
    [105, 'X-Tudo                 ',  'R$ 17,00', 17.00],
    [200, 'Refrigerante Lata      ',  'R$  5,00',  5.00],
    [201, 'Chá Gelado             ',  'R$  4,00',  4.00],
]

print('Bem vindo a lanchonete do RENAN')
print('*********************** CARDÁPIO ***********************')

#incrementação na lista de produtos
for prod in produtos:
    print('| {0} | {1}            |  {2} |'.format(prod[0], prod[1], prod[2]))

print('********************************************************')

# criação de Variáveis
incluirProduto = 1 #habilitando inclusão de produtos
total = 0
contador = 0
nomeProduto = ""
valorProduto = ""
produtosSelecionado = []

while incluirProduto:

    solicitarCodigoProduto = 1

    while solicitarCodigoProduto:

        codigoProduto = int(input('Entre com o código desejado: '))

        #  se o codigo informado e valido:
        if (100 <= codigoProduto <= 105) or (200 <= codigoProduto <= 201):

            for prod in produtos:
                if prod[0] == codigoProduto:
                    nomeProduto = prod[1]
                    valorProduto = prod[2]
                    total += prod[3]
                    produtosSelecionado.append(prod)
                    break

            # Print do produto selecionado
            print("Você pediu um {0} no valor de {1}".format(nomeProduto.rstrip(), valorProduto.strip()))

            break
        else: # quando a opção digitada é inválida
            print("Opção inválida")

    print('Deseja pedir mais alguma coisa?\n'
          '1 - Sim\n'
          '0 - Não')

    incluirProduto = int(input())

print('\n\n*********************** SUA CONTA **********************')
for prod in produtosSelecionado:
    print('| {0} | {1}            |  {2} |'.format(prod[0], prod[1], prod[2]))
print('********************************************************\n')
print("O total a ser pago é: R${0:.2f}".format(total))

