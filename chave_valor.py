#EX 1 - Criando os dicionarios vazios, seguido de atribuição de chave: valor
dic_1 = {}
dic_1['Nome'] = "Clark Cant"
dic_1['Idade'] = "790"
print(dic_1)

#EX 2 - Criando um dicionario com pares chave: valor
dic_2 = {"Nome": "Bruce Wayne", "Idade": 39}
print(dic_2)

#EX 3 - Criação de um dicionario com lista de tuplas representando pares chave: valor
dic_3 = dict([('Nome', 'Alisson'),('Idade', 28)])
print(dic_3)


#EX 4 - Criando um dicionario usando a função built-in zip() e duas listas, uma para as chaves e outra para os valores 
dic_4 = dict(zip(['Nome','Idade'], ['Ayrton Senna', 'F - 34']))
print(dic_4)

#Imprime se é verdadeiro ou falso
print(dic_1 == dic_2 == dic_3 == dic_4)