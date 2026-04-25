import random

from nicegui import ui

perguntas = [
    {'pergunta': 'Qual equipamento é mais adequado para separar líquidos imiscíveis?', 'opcoes': ['Funil de separação', 'Balança', 'Microscópio', 'Pipeta'], 'correta': 'Funil de separação'},
    {'pergunta': 'Qual é a função do condensador em um processo de destilação?', 'opcoes': ['Resfriar e condensar os vapores', 'Aumentar a temperatura da mistura', 'Separar os componentes por densidade', 'Medir a pressão do sistema'], 'correta': 'Resfriar e condensar os vapores'},
    {'pergunta': 'Qual equipamento é utilizado para medir a massa de um objeto?', 'opcoes': ['Balança', 'Microscópio', 'Pipeta', 'Funil de separação'], 'correta': 'Balança'},
    {'pergunta': 'Qual é a função de um microscópio?', 'opcoes': ['Aumentar a imagem de objetos pequenos', 'Separar líquidos imiscíveis', 'Medir a massa de um objeto', 'Resfriar vapores'], 'correta': 'Aumentar a imagem de objetos pequenos'},
    {'pergunta': 'Qual equipamento é utilizado para transferir líquidos em pequenas quantidades?', 'opcoes': ['Pipeta', 'Balança', 'Funil de separação', 'Microscópio'], 'correta': 'Pipeta'},
]

pontos = 0


@ui.page('/questoes')
def questoes_page():
    global pontos

    container = ui.column().classes('w-full h-screen flex items-center justify-center bg-white')
    perguntas_embaralhadas = random.sample(perguntas, len(perguntas))
    indice = 0
    limite = 3

    def mostrar_pergunta():
        nonlocal indice

        container.clear()

        if indice >= limite:
            with container:
                ui.label('Quiz finalizado!').classes('text-2xl')
            return

        pergunta_atual = perguntas_embaralhadas[indice]

        with container:
            with ui.card().classes('p-6 rounded-xl shadow bg-white'):
                ui.label(pergunta_atual['pergunta']).classes('w-full text-center text-2xl')

                for opcao in pergunta_atual['opcoes']:
                    def verificar_resposta(opcao=opcao):
                        nonlocal indice

                        if opcao == pergunta_atual['correta']:
                            ui.notify('Resposta correta!', color='positive')
                        else:
                            ui.notify('Resposta incorreta. Tente novamente.', color='negative')

                        indice += 1
                        mostrar_pergunta()

                    ui.button(opcao, on_click=verificar_resposta).style('width: 100%; margin-top: 10px')

    mostrar_pergunta()
