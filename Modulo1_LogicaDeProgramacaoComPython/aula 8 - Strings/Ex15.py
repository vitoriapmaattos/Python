"""
Escreva um algoritmo para validar se uma string é um endereço de e-mail
válido.
"""

import re

texto = """Durante os últimos anos, testemunhamos muitos eventos históricos 
e transformações. No dia 01/01/2000, muitos acreditavam que o mundo 
enfrentaria o chamado "bug do milênio", um problema de software que poderia 
fazer com que sistemas de computador falhassem. Felizmente, a maioria dos 
sistemas foi corrigida a tempo e não houve grandes interrupções.
Mais tarde, em 12/06/2010, uma das maiores Copas do Mundo da FIFA começou na 
África do Sul. Foi uma celebração incrível do esporte, e muitos ainda lembram 
do característico som das vuvuzelas.
A mudança climática também se tornou um foco global. Em 05/12/2015, foi 
assinado o Acordo de Paris, uma tentativa de países ao redor do mundo de 
combater as mudanças climáticas. Este acordo foi historicamente firmado após 
longas negociações.
Recentemente, em 20/03/2023, a conferência internacional sobre energias 
renováveis demonstrou novas tecnologias promissoras que podem nos levar a um 
futuro mais sustentável.
Em todas essas datas, observamos a humanidade enfrentando desafios e buscando 
soluções inovadoras. Certamente, haverá mais momentos memoráveis no futuro.
"""

padrao = r"\b\d{2}\/\d{2}\/\d{4}\b"

palavras = re.findall(padrao, texto)

print(*palavras, sep=", ")