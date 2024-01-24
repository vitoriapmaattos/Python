"""
Encontre todas as URLs no texto abaixo e devolva-as em uma lista. Use
expressões regulares.
"""
import re

texto = """
No mundo digital de hoje, muitos recorrem à internet para se atualizarem sobre 
as últimas novidades em tecnologia. O blog TechInsights, localizado em 
http://www.techinsights.com, é uma ótima fonte de artigos detalhados e análises 
de produtos recentes. Para aqueles que estão mais interessados em tutoriais e 
aprendizado prático, o site https://www.codeacademy.net oferece uma variedade 
de cursos em diferentes linguagens de programação.
Além desses, o recente fórum de discussão http://forum.digitaltalks.org tem se 
destacado como uma comunidade vibrante onde profissionais e entusiastas da 
tecnologia compartilham suas experiências, dúvidas e descobertas.
Se você está procurando por eventos ou conferências para participar, o site 
https://events.techtoday.com lista os principais acontecimentos no mundo da 
tecnologia ao longo do ano.
"""
url = []

padrao = r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}"
url.append(re.findall(padrao, texto))

print(url)
