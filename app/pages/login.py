from nicegui import ui


@ui.page('/login')
def login_page():
    def tentar_login():
        if nome_usuario.value == 'admin' and senha.value == '1234':
            ui.notify('Login realizado com sucesso!', color='positive')
            ui.navigate.to('/modos_jogos')
        else:
            ui.notify('UsuÃ¡rio ou senha incorretos', color='negative')

    with ui.column().classes('w-full h-screen flex items-center justify-center bg-white'):
        with ui.card().classes('p-6 rounded-xl shadow bg-white'):
            ui.label('Bem-vindo').classes('w-full text-center text-2xl')
            ui.label('Entre com o seu login e senha').classes('w-full text-center text-sm')

            ui.label('EMAIL').classes('text-xs')
            with ui.element('div').classes(
                'flex items-center gap-2 p-3 w-[448px] h-[60px] border-2 border-blue-500 rounded-lg '
                'cursor-pointer hover:bg-blue-50 transition-colors'
            ):
                ui.icon('login', color='blue').classes('text-2xl')
                nome_usuario = ui.input('Entrar no Sistema').props('borderless').classes('text-blue-500 font-bold')

            ui.label('SENHA').classes('text-xs')
            senha = ui.input(label='SENHA', password=True, password_toggle_button=True)

            ui.button('Login', color='tomato', on_click=tentar_login).style('width: 448px; height: 48px')
