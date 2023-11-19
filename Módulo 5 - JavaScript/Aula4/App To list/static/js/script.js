$(document).ready( () => {

    // Referências de elementos do DOM

    const $formCadastroTarefa = $("#form-cadastro-tarefa");
    const $alertCadastroTarefaErro = $("#alert-cadastro-tarefa-erro");
    const $btnClose = $('.btn-close');
    const $data = $('#data');
    const $alertCadastroTarefaSucesso = $("#alert-cadastro-tarefa-sucesso");
    const $tbodyTarefas = $("#tbody-tarefas")

    // Tirando o refresh após o submit do forms

    $formCadastroTarefa.submit(() => {
        const $tarefa = $('#tarefa').val();
        const $data = dayjs($('#data').val()).format("DD/MM/YYYY");

        // Exibindo mensagem de erro
        if (!$tarefa || !$data) {
            $alertCadastroTarefaErro.show();
            return false;
        }

        salvaTarefaEmLocalStorage($tarefa, $data);
    });

    // Adicionando a ação de alterar o disply quando fechar o alerta
    $btnClose.click(function () {
        $(this).parent().css("display", "none");
    });

    // Salvando a tarefa no localStorage e transformando em string e depois transformando em objeto novamente

    function salvaTarefaEmLocalStorage($tarefa, $data) {

        // Salvando em uma constante a tarefa, a data e criando um ID
        const objetoTarefaParaSalvar = { 
            id: new Date().getTime(), 
            $tarefa, 
            $data, 
            status:"Pendente",
        };

        // criando um array de strings e salvando como objetos
        const tarefasCadastradasEmLocalStorage = JSON.parse(localStorage.getItem("tarefas-todo-list"));

        // Conferindo se ja existe tarefa no array e acrescentando uma tarefa nova nessa array
        if (tarefasCadastradasEmLocalStorage && tarefasCadastradasEmLocalStorage.length){
            tarefasCadastradasEmLocalStorage.push(objetoTarefaParaSalvar);
        
            // Transformando o objeto em string e salvando como um Array
            localStorage.setItem("tarefas-todo-list", JSON.stringify(tarefasCadastradasEmLocalStorage));
            
        } else {
        // Se ainda não existir um Array, ira transformar o objeto em string e transformar em um Array para salvar as tarefas
        localStorage.setItem("tarefas-todo-list", JSON.stringify([objetoTarefaParaSalvar]));
        }

        // Exibindo mensagem de sucesso e limpando formulário
        $alertCadastroTarefaSucesso.show();
        $tarefa.val("");
        $data.val("");
    }

        // Montando tabela de tarefas

    function montaTabelaComTarefasDoStorage() {
        const tarefasCadastradasEmLocalStorage = getTarefasCadastradasEmLocalStorage();

        if (tarefasCadastradasEmLocalStorage.length) {
            for (let i = 0; i < tarefasCadastradasEmLocalStorage.length; i++) {
                $tbodyTarefas.append(
                    "<tr>" + 
                    "<td>" + tarefasCadastradasEmLocalStorage[i].$tarefa + "</td>" +
                    "<td>" + tarefasCadastradasEmLocalStorage[i].$data + "</td>" +
                    "<td>" + tarefasCadastradasEmLocalStorage[i].status + "</td>" +
                    "<td> Editar - Excluir </td>" +
                    "</tr>"
                );
            }
        } else {
            $tbodyTarefas.append("<h2>Não existem tarefas cadastradas</h2>");
        }
    }

    function getTarefasCadastradasEmLocalStorage () {
        return JSON.parse(localStorage.getItem("tarefas-todo-list")) || [];
    }

    // Criando tabela de tarefas
    montaTabelaComTarefasDoStorage();

    const createTask = (description, expirationDate, completed = false) => {
        const $li = $('<li class="list-group-item d-flex justify-content-between align-items-center"></li>');

        // Criando os elementos do checkbox
        const $checkboxDiv = $("<div>", {
            "class": "form-check d-flex align-items-center column-gap-2 checkbox-xl"
        });

        // Gerando um ID único para a checkbox (Para que ao clicar na label marque o checkbox :D)
        const checkboxId = generateRandomId("checkbox_");
        const $checkbox = $("<input>", {
            "class": "form-check-input",
            type: "checkbox",
            id: checkboxId,
            checked: completed
        });

        const $label = $("<label class='form-check-label'></label>").attr("for", checkboxId);
        const $description = $("<p class='fs-6 mb-0'></p>").text(description);
        const $expirationDate = $("<span class='text-secondary'></span>").text(`Expira em: ${expirationDate}`);
        
        // Adicionando a descrição e a data de expiração na label
        $label.append($description, $expirationDate);

        // Adicionando o checkbox e a label na DIV
        $checkboxDiv.append($checkbox, $label);

        // Criando os botões de editar e excluir
        const $buttonDiv = $("<div class='d-flex column-gap-2'></div>");
        const $editButton = createIconButton("bi bi-pencil", "btn btn-warning btn-sm", () => startEditTask($li)); // 4º Passo: criar a função de edição
        const $removeButton = createIconButton("bi bi-x-lg", "btn btn-danger btn-sm", () => onRemoveTask($li)); // 3º Passo: criar a função de remoção
        $buttonDiv.append($editButton, $removeButton);

        // Adicionando a div do checkbox e a div dos botões na tarefa
        $li.append($checkboxDiv, $buttonDiv);

        return $li;
    };

});