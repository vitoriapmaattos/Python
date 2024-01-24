// Tipos de dados
/* Dados Primitivos
    type number -> Valor Numérico
    type string -> Caractéres
    type boolean -> Verdadeiro ou falso
    type null -> Vazio (none/nulo)
    type undefined -> Quando não é atribuído um valor
*/

// Variáveis
/*
Forma antiga: var valor = 1; Não utilizar.

var valor = 1;
console.log(valor); // print java script

Forma atual: 
1- Forma principal
let valor = 1;
console.log(valor);

2- Forma secundária - Da pra utilizar mas não é recomendável.
valor = 1;
console.log(valor);
*/

// Cada tipo de dado:
let number = 1;
console.log(typeof number);

let string = "Hello World";
console.log(typeof string);

let boolean = true;
console.log(typeof boolean);

let nothing = null;
console.log(typeof nothing);

let notDefined;
console.log(typeof notDefined);

// type casting

console.log(typeof String(number))