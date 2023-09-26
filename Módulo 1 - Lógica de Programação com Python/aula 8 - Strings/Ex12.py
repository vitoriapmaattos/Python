"""
Escreva um algoritmo que substitua todos os e-mails em um texto por
[email protegido].
"""
import re

texto = """
Durante a conferência anual de tecnologia, muitos especialistas compartilharam 
seus contatos para colaborações futuras. Amanda Silva, uma renomada cientista 
de dados, mencionou que pode ser contatada através do e-mail 
amanda.silva@datasci.com. Pedro Alves, que apresentou os avanços mais recentes 
em inteligência artificial, também compartilhou seu contato: 
pedro.ai@techtalks.org. Além deles, Maria Fernanda, uma especialista em 
segurança cibernética, deu seu e-mail como referência para aqueles interessados 
em suas consultorias: maria.cybersec@securenet.net.
No entanto, foi recomendado que, ao enviar e-mails para eles, seja conciso e 
direto, pois costumam receber uma grande quantidade de mensagens diariamente.
"""

padrao = r"\w+\.+\w+@\w+\.\w+\."
subtexto = "[E-mail protegido]"

texto_novo = re.sub(padrao, subtexto, texto)

print(texto_novo)

