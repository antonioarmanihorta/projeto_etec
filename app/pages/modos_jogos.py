from nicegui import ui


@ui.page('/modos_jogos')
def modos_jogos_page():
    with ui.column().classes('w-full h-screen flex items-center justify-center bg-white'):
        ui.label('Selecione um modo de jogo').classes('text-xs')
        ui.label('Como vocÃª quer jogar hoje?').classes('text-5xl')

        with ui.row():
            with ui.card():
                with ui.column():
                    ui.html('<div class="flex items-center justify-center w-20 h-20 bg-blue-100 border-2 border-blue-500 rounded-lg"><i class="fa-solid fa-shuffle text-4xl text-blue-500"></i></div>')
                    ui.label('Aleatório').classes('text-2xl')
                    ui.label('Texto de descrição do modo de jogo aleatório')
                    ui.button('Selecionar', color='blue', on_click=lambda: ui.navigate.to('/questoes'))

            with ui.card():
                with ui.column():
                    ui.html('<div class="flex items-center justify-center w-20 h-20 bg-blue-100 border-2 border-blue-500 rounded-lg"><i class="fa-solid fa-sliders text-4xl text-blue-500"></i></div>')
                    ui.label('Filtrado').classes('text-2xl')
                    ui.label('Texto de descrição do modo de jogo filtrado')
                    ui.button('Selecionar', color='blue', on_click=lambda: ui.navigate.to('/questoes'))

        with ui.card():
            with ui.column():
                ui.html('<div class="flex items-center justify-center w-20 h-20 bg-blue-100 border-2 border-blue-500 rounded-lg"><i class="fa-solid fa-graduation-cap text-4xl text-blue-500"></i></div>')
                ui.label('Código do professor').classes('text-2xl')
                ui.label('Texto de descrição do modo de jogo código do professor')
                ui.button('Selecionar', color='blue', on_click=lambda: ui.navigate.to('/questoes'))

        ui.button('Ver histórico de partidas', color='blue', on_click=lambda: ui.navigate.to('/historico_jogador'))
