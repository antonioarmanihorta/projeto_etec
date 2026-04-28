from nicegui import ui

@ui.page('/add_question')
def add_question_page():

    estado = {'selecionado': None}
    botoes = {}

    def atualizar():
        for o, botao in botoes.items():

            '''
            if o == estado['selecionado']:
                botao.props('color=blue text-color=black') 
                #botao.remove_props('outline')
            else:
                botao.props('outline color=grey') #.remove_props('text-color')

            '''
            if o == estado['selecionado']:
                botao.set_color('blue')
            else:
                botao.set_color('grey')

    def clicar(opcao):

        if estado['selecionado'] == opcao:
            estado['selecionado'] = None
        else:
            estado['selecionado'] = opcao

        atualizar()

    with ui.column():
        with ui.card():
            ui.label("Enunciado")
            enunciado = ui.input()

            ui.label("Categoria")
            categoria = ui.input()

            ui.label("Alternativas (Selecione a correta)")

            with ui.column().classes('gap-2'):
                for opcao in ['A', 'B', 'C', 'D']:
                    botao = ui.button(
                        opcao,
                        on_click=lambda o=opcao: clicar(o)
                    ).classes('w-full')

                    botao.props('outline color=grey')
                    botoes[opcao] = botao
    ui.button("Adicionar pergunta")