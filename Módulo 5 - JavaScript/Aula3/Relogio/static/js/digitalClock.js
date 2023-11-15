$(document).ready(() => {
// Selecionando os elementos do DOM
const $clock = $(".clock");
const $date = $(".date");
const $toggleButton = $("#toggleButton");

/**
 *Atualiza o relógio
 */
const updateClock = () => $clock.text(new Date().toLocaleTimeString());

/**
 * Formata o dia da semana de número para o formato português
 * @param {number} dayOfWeek - Dia da semana 
 * @returns {string} dia da semana formatado
 */
const formatDayOfWeek = (dayOfWeek) => {
    const daysOfWeek = ["Domingo", "Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"];
    return daysOfWeek[dayOfWeek];
};

/**
 * Formata o mês de número para português
 * @param {number} month - número do mês 
 * @returns {string} dia do mês formatado
 */
const formatMonth = (month) => {
    const monthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
    return monthNames[month];
};

/**
 * Formata o dia do mês para que ele sempre possua duas casas
 * @param {number} day - dia do mês
 * @returns {string} dia do mês com duas casas
 */
const formatDay = (day) => String(day).padStart(2, "0");

/**
 * Atualiza a data
 */
const updateDate = () => {
    const today = new Date();
    const dayOfWeek = formatDayOfWeek(today.getDay());
    const month = formatMonth(today.getMonth());
    const day = formatDay(today.getDate());
    const year = today.getFullYear();
    
    $date.text(`${dayOfWeek}, ${day} de ${month} de ${year}`);
};

// setInterval() -> Executar uma ação em um determinado intervalo, para sempre!
// setTimeout -> Executar uma ação em um determinado intervalo, uma única vez.
// (função , tempo de execução em milisegundos)
let clockTimer = setInterval(updateClock, 1000); //let cria uma variável

//Controla o estado do relógio
let isPaused = false; //isPaused é uma boa prática para indicar constantes que são booleanas

//vai fazer a troca entre pausar e rodar
const toggleTimer = () => {
    isPaused = !isPaused; //falso passa a ser verdadeiro, verdadeiro passa a ser falso - negando o is
    if (isPaused){
        clearInterval(clockTimer);
        $toggleButton.text("Resumir");
        $toggleButton.css("background-color","#ADE25D");
    } else {
        updateClock();
        clockTimer = setInterval(updateClock, 1000);
        $toggleButton.text("Pausar");
        $toggleButton.css("background-color","rgb (6, 164, 236)");
    }
};

//atrelando o evento de click ao botão pausar
$toggleButton.click(toggleTimer);


updateClock();
updateDate();

});
