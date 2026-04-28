from nicegui import ui
from app.pages import historico_jogador, login, modos_jogos, questoes, teacher, classroom_code, add_question

ui.add_head_html(
    '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
''',
    shared=True,
)


@ui.page('/')
def indice():
    ui.navigate.to('/login')


ui.run()
