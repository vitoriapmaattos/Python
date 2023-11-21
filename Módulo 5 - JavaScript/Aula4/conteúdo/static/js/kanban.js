$(document).ready(() => {
    // Selecionar os elementos
    const $form = $("#addTaskForm")
    const $descriptionInput = $("#descriptionInput")
    const $boardSelect = ("#boardSelect")
    const $modal = new bootstrap.Modal("addTaskModal")

    const createIconButton = (iconClass, btnClasses, clickHandler) => {
        const $button = $("<button></button>").addClass(btnClasses)
        const $icon = $("<i></i>").addClass(iconClass)
        $button.append($icon)
        $button.click(clickHandler)
        return $button
    }
    const addTaskToBoard = (decription, board) => {
        const $newTask = $("<div></div>").addClass("kanban-item")
        const $taskText = $("<span></spam>").text(description)
        const $editButton = createIconButton("bi bi-pencil", "btn btn-warning btn-sm", () => {
            const editedText = prompt("Nova descrição", description)
            if (editedText) {
                $tashText.text(editedText)
            }
        })

        const $deleteButton = createIconButton("bi-bi-x", "btn btn-wdanger btn-sm", () => {
            $newTask.remove()
        })

        const $buttonsContainer = $("<div></div>").addClass("d-flex column-gap-2")
        $buttonsContainer.append($editButton, $deleteButton)
        $newTask.append($taskText, $buttonsContainer)
        $(`#${board}`).append($newTask)
    }

    // Evento para a submissão do formulário
    $form.submit(event => {
        // Através do evento que conseguimos cancelar o comportamento padrão do envio do formulário (recarregar a página)
        event.preventDefault()

        // Verificar se o elemento é válido
        if ($form[0].checkValidity()) {
            // Adicionar tarefa
            addTaskToBoard($descriptionInput.val(), $boardSelect.val())
            $form[0].reset()
            $modal.hide()
            $form.removeClass("was-validated")
        } else {
            $form.addClass("was-validated")
        }
    })

    $(".kanban-column").sortable({
        connectWith: ".kanban-column", cursor:"grab"
    }).disableSelection()
})