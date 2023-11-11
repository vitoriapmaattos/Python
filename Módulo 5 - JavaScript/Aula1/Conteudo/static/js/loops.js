// WHILE
let i = 0; // variável
while (i < 3) {
    alert(i);
    i++; //incrementar variável  ++ soma 1 -- diminui 1 i += 2 soma 2
}

//FOR (COMEÇO; CONDIÇÃO; INCREMENTO)
for (let i = 0; i < 4; i++){
    alert(i);
}

// WHILE TRUE

let sum = 0;
while (true){
    const value = +prompt("Digite um número:");

    if (!value) break;

    sum += value;
}

alert(`O resultado da soma foi: ${sum}`);

for (let i = 0; i <= 10; i++) {
    if (i % 2 !== 0) continue;
    alert (i);
}