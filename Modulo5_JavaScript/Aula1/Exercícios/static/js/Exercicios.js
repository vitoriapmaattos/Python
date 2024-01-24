/*
VARIÁVEIS - https://javascript.info/variables#tasks
Exercício 1

let name = "John";

let admin = name;

alert(admin);

Exercício 2

let ourPlanetName = "Terra";

let currentUserName = prompt("Digite o seu nome:");

Exercício 3

const BIRTHDAY = "18.04.1982"; // birthday em maiúscula

const age = someCode(BIRTHDAY); // age em minúscula, pois a váriável muda a cada ano

TIPOS DE DADOS - https://javascript.info/types#tasks
Exercício 1

let name1 = "Ilya";

alert(`hello ${1}`); // number 1

alert(`hello ${"name"}`); // string "name"

alert(`hello ${name1}`); //string "Ilya"

INTERAÇÃO - https://javascript.info/alert-prompt-confirm#tasks
Exercício 1

let currentUserName1 = prompt("Digite seu nome: ");

alert(currentUserName1);

OPERAÇÕES - https://javascript.info/operators#tasks
Exercício 1

let a = 1, b = 1;

let c = ++a; // 2 forma prefix altera imediatamente

let d = b++; // 1 forma postfix altera mas entrega o valor anterior

alert(a);
alert(b);
alert(c);
alert(d);

EXERCÍCIO 2

let a = 2;

let x = 1 + (a *= 2); 

a = 4 - x = 5

EXERCÍCIO 3


"" + 1 + 0 // 10
"" - 1 + 0 // -1
true + false // 1
6 / "3" // 2
"2" * "3" // 6
4 + 5 + "px" // 9px
"$" + 4 + 5 // $45
"4" - 2 // 2
"4px" - 2 // NaN
"  -9  " + 5 // -9 5
"  -9  " - 5 // -14
null + 1 // 1
undefined + 1 // NaN
" \t \n" - 2 // -2

EXERCÍCIO 4

let a = +prompt("First number?", 1);
let b = +prompt("Second number?", 2);

alert (a + b);

COMPARAÇÕES - https://javascript.info/comparison#tasks
EXERCICIO 1

5 > 4 // true
"apple" > "pineapple" // false
"2" > "12" // true
undefined == null // true
undefined === null // false
null == "\n0\n" // false
null === +"\n0\n" // false


IF E ELSE - https://javascript.info/ifelse#tasks
EXERCÍCIO 1

if ("0") {
    alert( 'Hello' );
  }

SIM, ALERT É MOSTRADO

EXERCÍCIO 2

let nameOficial = prompt("Qual o nome oficial do JavaScript?")
if (nameOficial == "ECMAScript") {
    alert("Rigth!");
} else {
    alert("You don't know? “ECMAScript”!");
}

EXERCICIO 3


let number = +prompt("Digite um número:")

if (number > 0) {
    alert("1");
} else if (number == 0 ) {
    alert("0");
} else {
    alert("-1");
}

EXERCICIO 4

let result = (a + b < 4) ? 'Below' : 'Over';

EXERCÍCIO 5

let message = (login == 'Employee') ? 'Hello' :
  (login == 'Director') ? 'Greetings' :
  (login == '') ? 'No login' :
  '';

OPERADORES LÓGICOS - https://javascript.info/logical-operators#tasks
EXERCICIO 1

alert( null || 2 || undefined ); 
// 2 é o primeiro valor verdadeiro

EXERCÍCIO 2

alert( alert(1) || 2 || alert(3) );
// Alert 1 e depois o 2

EXERCÍCIO 3

alert( 1 && null && 2 );
// Alert null

EXERCICIO 4

alert( alert(1) && alert(2) );
// Alert 1 e undefined

EXERCÍCIO 5

alert( null || 2 && 3 || 4 );
// Alert 3

EXERCÍCIO 6

let age = +prompt("Qual a sua idade?");

if ( age >= 14 && age <= 90) {
    alert("SIM!");
} else {
    alert("NÂO!");
}

EXERCICIO 7

let age = +prompt("Qual a sua idade?");

if ( age < 14 || age > 90) {
    alert("NÃO!");
} else {
    alert("SIM!");
}

EXERCICIO 8

if (-1 || 0) alert( 'first' ); //É executado
if (-1 && 0) alert( 'second' ); //Não é executado
if (null || -1 && 1) alert( 'third' ); //É executado

EXERCICIO 9

let user = prompt("Digite o usuário: ");

if ( user == "Admin" ) {
    let password = prompt("Digite a senha:");
    if (password == "TheMaster") {
        alert("Welcome!");
    } else if (password === '' || password === null) {
        alert("Cancelado");
    } else {
        alert("Senha Errada");
    }  
} else if ( user === '' || user === null ) {
    alert("Cancelado");
} else {
    alert("Não te conheço")
}

LAÇOS DE REPETIÇÃO - https://javascript.info/while-for#tasks

EXERCICIO 1

let i = 3;

while (i) {
  alert( i-- );
}

Último valor ofertado é 1, pois a cada alert diminui um do i

EXERCICIO 2

Forma Pré-Fixada
let i = 0;
while (++i < 5) alert( i );

Forma Pós-Fixada
let i = 0;
while (i++ < 5) alert( i );

Na forma pós-fixada o número limite é incluido, como um < ou =. Ja na forma pré-fixada o número limite não é incluído.

EXERCÍCIO 3

Da mesma forma que o while o pós-fixado inclui o número limite e o pré-fixado não, porém o for incluí tbm o número informado 
no i e após começa a acrescentar os valores em i.

A forma pós-fixada:
for (let i = 0; i < 5; i++) alert( i );

A forma do pré-fixado:
for (let i = 0; i < 5; ++i) alert( i );

EXERCICIO 4

for (let i = 2; i <= 10; i++) {
    if (i % 2 == 0) {
    alert( i );
    }
};

EXERCICIO 5

Fazendo com for:
for (let i = 0; i < 3; i++) {
    alert( `number ${i}!` );
}

Fazendo com while:
let i = 0;
while (i++ < 3) alert( `number ${i}!`);

EXERCICIO 6

let num;

do {
  num = prompt("Digite um número", 0);
} while (num <= 100 && num);

SWITCH - https://javascript.info/switch#tasks

EXERCICIO 1

if(browser == 'Edge') {
  alert("You've got the Edge!");
} else if (browser == 'Chrome'
 || browser == 'Firefox'
 || browser == 'Safari'
 || browser == 'Opera') {
  alert( 'Okay we support these browsers too' );
} else {
  alert( 'We hope that this page looks ok!' );
}

EXERCICIO 2

let a = +prompt('a?', '');

switch (a) {
  case 0:
    alert( 0 );
    break;

  case 1:
    alert( 1 );
    break;

  case 2:
  case 3:
    alert( '2,3' );
    break;
}

FUNÇÕES - https://javascript.info/function-basics#tasks

EXERCICIO 1

Existe alguma diferença na execução da função, se retirar o else como na segunda função?

function checkAge(age) {
    if (age > 18) {
      return true;
    } else {
      return confirm('Seus pais permitiram?');
    }
}

function checkAge(age) {
if (age > 18) {
    return true;
}
return confirm('Did parents allow you?');
}

Não há diferença! As duas funções funcionam da mesma forma.

EXERCICIO 2

Outras duas formas de executar a mesma função:

function checkAge(age) {
  return (age > 18) ? true : confirm('Did parents allow you?');
}

function checkAge(age) {
  return (age > 18) || confirm('Did parents allow you?');
}

ARROW FUNCTIONS - https://javascript.info/arrow-functions-basics#tasks

EXERCICIO 1

Substitua Expressões de Função por funções de seta no código abaixo:

function ask(question, yes, no) {
  if (confirm(question)) yes();
  else no();
}

ask(
  "Do you agree?",
  function() { alert("You agreed."); },
  function() { alert("You canceled the execution."); }
);

-

function ask(question, yes, no) {
  if (confirm(question)) yes();
  else no();
}

ask(
  "Do you agree?",
  () => alert("You agreed."),
  () => alert("You canceled the execution.")
);
*/