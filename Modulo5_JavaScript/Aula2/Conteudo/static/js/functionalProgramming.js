// Princípios  da Programação Funcional

// 1) Imutabilidade
// 2) Funções Puras

/* Exemplo de função pura

let contador = 0;

function modificaContador () {
    contador++;
}

modificaContador(); */

const people = [
    { name: "John", age: 22 },
    { name: "Mary", age: 16 },
    { name: "Peter", age: 23 }
];

// Map
const peopleNames = people.map((person, index) => `Pessoa ${index + 1}: ${person.name}`);

// Filter
const minors = people.filter(person => person.age < 18);

// Reduce - reduzindo vetores valor em um número só
//accumulator = 0
//accumulator = 0+22 = 22
//accumulator = 22+16 = 38
//accumulator = 38+23 = 61
const sumOfAges = people.reduce((accumulator, person) => accumulator + person.age, 0);

// Sort - vai mudar o objeto/dicionário, não é ideal
people.sort((a, b) => a.age - b.age);

// A boa prática
const peopleOrderedByAge = [ ... people].sort((a, b) => a.age - b.age);