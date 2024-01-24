/**
 * Mostra uma mensagem no navegador.
 * @param {string} from - Quem esta enviando a mensagem.
 * @param {string} message - Mensagem que será mostrada.
 */
function showMessage(from, message = "Mensagem não fornecida") {
    alert(`${from}: ${message}`);
}

//showMessage("William", "Declarando funções!");
//showMessagem("Desconhecido");

console.log(sum(10, 2));

//Sintaxe normal

/**
 * Retorna a soma de dois números
 * @param {number} n1 
 * @param {number} n2 
 * @returns {number}
 */
//cont sum = (n1, n2) -> n1 + n2

function sum(n1, n2) {
    return n1 + n2;
}

console.log(sum(10, 2));

// Arrow functions
//Multiplique arrow function

/**
 * Retorna o dobro de um número
 * @param {number} n 
 * @returns {number}
 */

const double = n => n * 2;
console.log(double(3));

// Multiline arrow function
/**
 * Retorna a subtração de um número por outro
 * @param {number} n1 
 * @param {number} n2 
 * @returns {number}
 */

const sub = (n1, n2) => {
    const result = n1 - n2;
    return result;
}

// Função anônima
const quadrado = function(n) {
    return n * n;
}

console.log(quadrado(5));

// IIFE
(function () {
    alert("IIFE");
})();

// IIFE com arrow function

(() => {
    alert("IIFE com arrow function");
})();