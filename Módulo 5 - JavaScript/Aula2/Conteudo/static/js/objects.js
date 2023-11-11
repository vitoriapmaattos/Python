// Criando um objeto (dicionário python)

const user = {
    name: "Will",
    age: 23,
    "hair-color":"black", //declara como string quando o nome tem caractere especial
};

// Obtendo os valores
console.log(Object.values(user));

// Obtendo as chaves
console.log(Object.keys(user));

// Destructuring - Desestruturação, fazer uma cópia profunda
const userCopy = { ... user };

const numbers = [1, 2, 3, 4, 5];
const numbersCopy = [... numbers ]; 

//Conchetes para dicionários/objetos e Chaves para listas/array

