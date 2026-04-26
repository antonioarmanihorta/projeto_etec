from nicegui import ui

@ui.page('/classroom_code')
def classroom_code_page():
    with ui.column():
        with ui.card():
            with ui.card():
                ui.label("Compartilhe este código")
        ui.label("Nº de perguntas")
        ui.label("Dificuldade")
        ui.toggle(["Fácil", "Médio", "Difícil"], value="Fácil")
