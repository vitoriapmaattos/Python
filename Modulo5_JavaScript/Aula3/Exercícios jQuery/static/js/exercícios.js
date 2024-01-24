document.oncontextmenu = new Function("return false;");
//Exercício 2
//Desativando o botão direito

const $clickerButton = $("#clicker");
const $secret = $("#secret");
const $counter = $("counter").val(0);

//Exercício 1

let isSecret = false;

const clicker = () => {
    isSecret = !isSecret;
    if (isSecret) {
        $secret.show();
        $clickerButton.text("Ocultar");
    } else {
        $secret.hide();
        $clickerButton.text("Mostrar");
    }
};
$clickerButton.click(clicker);

// Exercício 3

$(document).ready(() => {
    const $counter = $('.counter');
    const $increment = $('#increment');
    const $decrement = $('#decrement');
    
    let counter = 0;

    const updateDisplay = () => {
        $counter.text(counter);
    };

    const incrementCounter = () => {
        counter++;
        updateDisplay();
    };

    const decrementCounter = () => {
        counter--;
        updateDisplay();
    };

    $decrement.click(decrementCounter);
    $increment.click(incrementCounter);
});

//Exercicio 4
const timerEl = document.getElementById('timer');
const marksList = document.getElementById('marks-list');

let intervalId = 0;
let timer = 0; // Armazena o teepo em centesimos de segundos, que vão se transformar em segundos, minutos e horas
let marks = []; // Armazena as marcações

// Função formatando o tempo
const formatTime = (time) => {
    const hours = Math.floor(time / 360000);
    const minutes = Math.floor((time % 360000) / 6000);
    const seconds = Math.floor((time % 6000) / 100);
    const hundredths = time % 100;

    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}:${hundredths.toString().padStart(2, '0')}`;
}

// Setando o tempo
const setTimer = (time) => {
    timerEl.innerText = formatTime(time);
}

// Adicionando a marcação
const addMarkToList = (markIndex, markTime) => {
    marksList.innerHTML += `<p>Marca ${markIndex}: ${formatTime(markTime)}</p>`;
}

// Incrementando o tempo
const toggleTimer = () => {
    const button = document.getElementById('power');
    const action = button.getAttribute('action');

    clearInterval(intervalId);

    if (action =='start' || action == 'continue') {
        intervalId = setInterval(() => {
            timer += 1;
            setTimer(timer)
        }, 10);
        button.setAttribute('action', 'pause');
        button.innerHTML = '<i class="bi bi-pause-btn"></i>';
    } else if (action == 'pause') {
        button.setAttribute('action', 'continue');
        button.innerHTML = '<i class="bi bi-play-circle"></i>';
    }
}

// Marcando o tempo e salvando na lista
const markTime = () => {
    marks.push(timer);
    addMarkToList(marks.length, timer);
}

// Resetar o cronometro e a marcação
const resetTimer = () => {
    clearInterval(intervalId);
    timer = 0;
    marks = [];
    setTimer(timer);
    marksList.innerHTML = '';
    const button = document.getElementById('power');
    button.setAttribute('action', 'start');
    button.innerHTML = '<i class="fa-solid fa-play"></i>';
}

// Evento de Click
document.getElementById('power').addEventListener('click', toggleTimer);
document.getElementById('mark').addEventListener('click', markTime);
document.getElementById('reset').addEventListener('click', resetTimer);

//Exercício 5

// boa prática para não ter acesso público as variáveis e para o documento todo ser lido antes do script ser realizado
const people = [
    { id: 1, name: "Ana", age: 23, sex: "F" },
    { id: 2, name: "Maria", age: 42, sex: "F" },
    { id: 3, name: "João", age: 15, sex: "M" },
    { id: 4, name: "Matheus", age: 19, sex: "M" },
    { id: 5, name: "Antônio", age: 40, sex: "M" },
];

//selecionando a tabela
const tableBody = document.querySelector("#peopleTable tbody");

//Documentando a função
/** Função para formatar sexo
 * @param {string} sex - O sex abreviado
 * @returns {string}
*/
const formatSex = sex => sex == "M" ? "Masculino" : "Feminino"

//criando as linhas com os dados
// jeito jquery 
$.each(people, (_, person) => {
    //Criando a linha com os dados da pessoa e inserindo na tabela
    const row = tableBody.insertRow();
    row.insertCell(0).textContent = person.id;
    row.insertCell(1).textContent = person.name;
    row.insertCell(2).textContent = person.age;
    row.insertCell(3).textContent = formatSex(person.sex)
});

//Exercicio 6
$(".grid-item").click(function () {
    // Remove a classe 'selected' de todas as divs
    $(".grid-item").removeClass("selected");

    // Adiciona a classe 'selected' à div clicada
    $(this).addClass("selected");

    // Atualiza o texto do parágrafo
    var selectedSquare = $(this).text();
    $("#selected-square").text(selectedSquare);
});