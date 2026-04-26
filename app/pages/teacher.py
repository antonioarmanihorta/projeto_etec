from nicegui import ui

@ui.page('/teacher')
def teacher_page():
    ui.button("Voltar", color="gray", on_click=lambda: ui.navigate.to('/login')).style('position: absolute; top: 20px; left: 20px;')
    ui.label("Identifica lab").style('position: absolute; top: 20px; right: 100px;')
    with ui.column().classes('w-full h-screen flex items-center justify-center bg-white'):
        ui.label('Área do Professor!')
        ui.label('Bem-vindo, Professor!')
        with ui.row():
            with ui.card().classes('w-[328px] h-[300px]'):
                ui.html('<div class="flex items-center justify-center w-20 h-20 bg-blue-100 border-2 border-blue-500 rounded-lg"><i class="fa-solid fa-user-group text-4xl text-blue-500"></i></div>')
                ui.label("Sala da turma")
                ui.label("Adicionar texto de descrição da sala da turma")
                ui.button("Criar sala", color="yellow")
            with ui.card().classes('w-[328px] h-[300px]'):
                ui.html('<div class="flex items-center justify-center w-20 h-20 bg-blue-100 border-2 border-blue-500 rounded-lg"><i class="fa-solid fa-chart-column text-4xl text-blue-500"></i></div>')
                ui.label("Relatório")
                ui.label("Adicionar texto de descrição do relatório")
                ui.button("Ver relatório", color="green")
        with ui.row():
            with ui.card().classes('w-[328px] h-[300px]'):
                ui.html('<div class="flex items-center justify-center w-20 h-20 bg-blue-100 border-2 border-blue-500 rounded-lg"><i class="fa-solid fa-pen-to-square text-4xl text-blue-500"></i></div>')
                ui.label("Perguntas")
                ui.label("Adicionar texto de descrição das perguntas")
                ui.button("Gerenciar  perguntas", color="blue")
            with ui.card().classes('w-[328px] h-[300px]'):
                ui.html('<div class="flex items-center justify-center w-20 h-20 bg-blue-100 border-2 border-blue-500 rounded-lg"><i class="fa-solid fa-tasks text-4xl text-blue-500"></i></div>')
                ui.label("Tarefas")
                ui.label("Adicionar texto de descrição das tarefas")
                ui.button("Abrir tarefas", color="orange")