"""
Crie um algoritmo que mapeie palavras em inglês para a sua tradução em um
dicionário, após isso peça para o usuário digitar um texto em inglês com as
palavras contidas no dicionário e mostre o texto traduzido.
"""
dic = {'blue': 'azul', 'pink': 'rosa', 'red': 'vermelho', 'green': 'verde'}

palavra = input("Digite uma cor em inglês: ")
print(''.join(dic[palavra]))
