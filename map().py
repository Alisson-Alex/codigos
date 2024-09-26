preco_em_dolar = [280, 300, 50, 800, 1299, 19]
cambio = 5.25
taxadd = 80
porcent = 100
preco_em_reais = list(map(lambda x: x * cambio, preco_em_dolar))
taxa = list(map(lambda y: y * taxadd, preco_em_reais))
taxa = list(map(lambda r: r / porcent, taxa))
valor_final = list(map(lambda k: k + taxa, preco_em_reais))
print(f"O preço dos itens em dolares eram: {preco_em_dolar}\n")
print(f"Agora faz o L: {valor_final}\n")