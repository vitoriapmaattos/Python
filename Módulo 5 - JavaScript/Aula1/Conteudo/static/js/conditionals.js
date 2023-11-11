const javascriptAge = +prompt("Quantos anos o JavaScript possui?")
// IF ELIF E ELSE
if (javascriptAge > 27) {
    alert("A idade digitada é maior do que a real");
} else if (javascriptAge < 27) { //elif
    alert("A idade digitada é menor do que a real");
} else {
    alert ("Você acertou!");
}

const currentHour = new Date().getHours();
alert(currentHour);

// AND &&
if (currentHour > 7 && currentHour > 19) {
    alert("O escritório está aberto.");
} else {
    alert ("O escritório está fechado");
}

// OR ||
if (currentHour < 8 || currentHour > 18) {
    alert("O escritório está fechado.");
} else {
    alert ("O escritório está aberto");
}

//NOT
alert(!true);

//IGUALDADE ===

// DIFERENTE !==

// o - Janeiro
// 1 - Fevereiro
const currentMonth = new Date().getMonth() + 1;

switch (currentMonth) {
    case 1:
        alert("Janeiro");
        break;

    case 2:
        alert("Fevereiro");
        break;

    case 3:
        alert("Março");
        break;
    case 4:
    case 5:
    case 6:
    case 7:
    case 8:
    case 9:
    case 10:
    case 11:
    case 12:
        alert("Outros Meses");
        break

    default:
        alert("Mês Inválido");
        break;
}