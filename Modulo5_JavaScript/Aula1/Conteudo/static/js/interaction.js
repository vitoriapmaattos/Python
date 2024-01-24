alert("Hello World"); //Serve para abrir uma caixa de alerta ao atualizar a página
const birthYear = +prompt("Em qual ano você nasceu?"); //constante de valor fixo, dependendo do usuário
const PI = prompt("Qual o valor de PI?"); //constante de valor fixo, em letras maiúsculas
const currentYear = prompt("Qual o Ano Atual?", new Date().getFullYear()); //constante de valor fixo, com autocomplete
const age = currentYear - birthYear;
alert(`Você tem ${age} anos de idade`);

/* função: 
new Date() - vai pegar a data atual completa
.getFullYear() - vai pegar o ano.
*/

/*
prompt = pede a informação para o usuário, informação vem em string ou null(quando o usuário não preencher)
+prompt = converte em number

cont -> cria e armazena o prompt em uma constante
*/
// print (f"Você tem {age} anos de idade") - como fazíamos no python