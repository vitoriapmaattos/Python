// Criando um array
const colors = ["red", "green", "blue" , "black", "white"]; //criando uma lista

// Consultando o tamanho do array
console.log(colors.length);

// Adicionando um elemento na lista
colors.push("yellow");

// Fatiamento do array
console.log(colors.slice(0, 2));

// Remover um elemento do array
colors.pop(); //remover o último elemento

colors.splice(0, 1); //remover pelo índice

//Iterando em um array
for (let i = 0; i < colors.length; i++) {
    console.log(colors[i]);
}

for (let color of colors) {
    console.log(color);
}

colors.forEach((item, index, array) => {
    console.log(`${item} está no índice ${index} do array ${array}`)
});