/*
OBJETOS - https://javascript.info/object#tasks

EXERCÍCIO 1
const user = {}; //criando um objeto vazio
user.name = "John"; // incluindo uma propriedade nome no objeto
user.surname = "Smith"; // incluindo uma propriedade sobrenome no objeto
user.name = "Pete"; // alterando a nome armazenado na propriedade
delete user.name; // deletando a propriedade nome

console.log(user);

EXERCÍCIO 2

function isEmpty(obj) {
    for (let key in obj) {
      return false;
    }
    return true;
  }

EXERCÍCIO 3


let salaries = {
    John: 100,
    Ann: 160,
    Pete: 250
}

let resultado = 0;
for (let key in salaries) { //percorre todos as chaves existentes dentro do obejto/dicionário salaries
    resultado += salaries[key]; //soma no resultado os valores existentes no objeto
}
alert(resultado);

EXERCÍCIO 4

let menu = {
    width: 200,
    height: 300,
    title: "My menu"
};

function multiplyNumeric(obj) {
    for (let key in obj) {
      if (typeof obj[key] == 'number') {
        obj[key] *= 2;
      }
    }
  }

multiplyNumeric(menu);

MÉTODOS DE OBJETOS - https://javascript.info/keys-values-entries#tasks

EXERCICIO 1

let salaries = {
    "John": 100,
    "Pete": 300,
    "Mary": 250
  };
  
function sumSalaries(salaries) {
    let sum = 0;
    for (let salary of Object.values(salaries)) {
    sum += salary;
}
    return sum;
}

alert( sumSalaries(salaries) )

EXERCICIO 2

let user = {
    name: 'John',
    age: 30
};

function count(obj) {
    return Object.keys(obj).length;
}

alert(count(user))

ARRAYS - https://javascript.info/array#tasks

EXERCICIO 1

let fruits = ["Apples", "Pear", "Orange"];

// Incluido um novo valor em fruits
let shoppingCart = fruits;
shoppingCart.push("Banana");

// Quantas frutas tem na lista
alert( fruits.length ) //4

EXERCICIO 2

let styles = ["Jazz", "Blues"];

alert(styles);

styles.push("Rock-n-Roll");

alert(styles);

styles[Math.floor((styles.length - 1) / 2)] = 'Clássicos'; // encontrando a chave do meio do objeto

alert(styles);

alert (styles.shift());

alert(styles);

styles.push("Reggae", "Rap");

alert(styles);

EXERCICIO 3

let arr = ["a", "b"];

arr.push(function() {
  alert( this );
});

arr[2]()

EXERCICIO 4

function sumInput() {
    let totals = [];

    while (true){

    const value = +prompt("Digite um número:",);

    if (!value) break;

    totals.push(+value);
    }

    let sum = 0;
    for (let total in totals) {
        sum += total;
    }
    return sum;
}

alert(sumInput());

EXERCICIO 5 

function getMaxSubSum(arr) {
  let maxSum = 0;
  let partialSum = 0;

  for (let item of arr) { // for each item of arr
    partialSum += item; // add it to partialSum
    maxSum = Math.max(maxSum, partialSum); // remember the maximum
    if (partialSum < 0) partialSum = 0; // zero if negative
  }

  return maxSum;
}

alert( getMaxSubSum([-1, 2, 3, -9]) ); // 5
alert( getMaxSubSum([-1, 2, 3, -9, 11]) ); // 11
alert( getMaxSubSum([-2, -1, 1, 2]) ); // 3
alert( getMaxSubSum([100, -9, 2, -3, 5]) ); // 100
alert( getMaxSubSum([1, 2, 3]) ); // 6
alert( getMaxSubSum([-1, -2, -3]) ); // 0


MÉTODO DE ARRAYS - https://javascript.info/array#tasks

EXERCICIO 1

function camelize(str) {
  return str
    .split('-') // splits 'my-long-word' into array ['my', 'long', 'word']
    .map(
      // capitalizes first letters of all array items except the first one
      // converts ['my', 'long', 'word'] into ['my', 'Long', 'Word']
      (word, index) => index == 0 ? word : word[0].toUpperCase() + word.slice(1)
    )
    .join(''); // joins ['my', 'Long', 'Word'] into 'myLongWord'
}

EXERCICO 2

/**
 * Filtra um vetor de acordo com um valor mínimo e máximo
 * @param {Array[]} arr - vetor a ser filtrado
 * @param {number} a - valor mínimo do intervalo
 * @param {number} b - valor máximo do intervalo
 * @returns {Array[]} - o vetor filtrado
 */
/*
const filterRange = (arr, a, b) => {
    return arr.filterRange(item => item >= a && item <= b)
}

let arr = [5, 3, 8, 1];
let filtered = filterRange (arr, 1, 4);
console.log(filtered);
console.log(arr);

EXERCICIO 3

function filterRangeInPlace(arr, a, b) {

  for (let i = 0; i < arr.length; i++) {
    let val = arr[i];

    // remove if outside of the interval
    if (val < a || val > b) {
      arr.splice(i, 1);
      i--;
    }
  }
}

let arr = [5, 3, 8, 1];

filterRangeInPlace(arr, 1, 4); // removed the numbers except from 1 to 4

alert( arr ); // [3, 1]

EXERCICIO 4

let arr = [5, 2, 1, -10, 8];

arr.sort((a, b) => b - a);

alert( arr );

EXERCICIO 5

function copySorted(arr) {
  return arr.slice().sort();
}

let arr = ["HTML", "JavaScript", "CSS"];

let sorted = copySorted(arr);

alert( sorted );
alert( arr );

DATAS - https://javascript.info/date#tasks

EXERCICIO 1

let data = new Date(2012, 1, 20, 3, 12);
alert(data);

EXERCICIO 2

function getWeekDay(date) {
  let days = ['SU', 'MO', 'TU', 'WE', 'TH', 'FR', 'SA'];

  return days[date.getDay()];
}

let date = new Date(2014, 0, 3);
alert( getWeekDay(date) );

EXERCICIO 3

function getLocalDay(date) {

    let day = date.getDay();
  
    if (day == 0) {
      day = 7;
    }
  
    return day;
  }

EXERCICIO GET AVERAGE AGE

let John = {
    name: "John",
    age: 25
};

let Pete = {
    name: "Pete",
    age: 30
};

let Mary = {
    name: "Mary",
    age: 29
};

let arr = [John, Pete, Mary];


const getAverageAge = (arr) => arr.reduce((acc, val)) ; acc + val.age, 0 / arr.length;
alert(getAverageAge(arr));
*/