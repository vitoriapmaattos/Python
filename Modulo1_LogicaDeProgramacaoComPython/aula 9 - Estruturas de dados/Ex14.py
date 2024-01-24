"""
 Imagine que você recebe logs de acessos a um site na seguinte estrutura:

logs = [
	{"usuario": "alice", "pagina": "/inicio"},
	{"usuario": "bob", "pagina": "/produtos" },
	{"usuario": "alice", "pagina": "/contato" },
	{"usuario": "carol", "pagina": "/sobre" }
]

"""
logs = [
	{"usuario": "alice", "pagina": "/inicio"},
	{"usuario": "bob", "pagina": "/produtos" },
	{"usuario": "alice", "pagina": "/contato" },
	{"usuario": "carol", "pagina": "/sobre" }
]

contagem_acessos = {}
for log in logs:
    usuario = log["usuario"]
    pagina = log["pagina"]

    #Caso o usuário não esteja na contagem, adicionar usuário
    if usuario not in contagem_acessos:
        contagem_acessos[usuario] = {}

    #Caso o usuário não tenha acessado a página ainda, adicionar a contagem da págia para o usuário
    if pagina not in contagem_acessos[usuario]:
        contagem_acessos[usuario][pagina] = 0

    contagem_acessos[usuario][pagina] += 1

print(contagem_acessos) 
