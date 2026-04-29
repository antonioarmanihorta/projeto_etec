perguntaAserAdd = []
respostasDaQuestao = []

def addQuestoes():
    cont = 1
    
    while cont == 1:
        questaoAserAdd = input("Digite a pergunta da questão a ser adicionada!\n")
        perguntaAserAdd.append(questaoAserAdd)
        
        for i in range(4):
            resposta = input(f"Adicione a resposta {i + 1} à pergunta a ser adicionada!\n")
            respostasDaQuestao.append(resposta)
            
        opcaoPerg = 0 
        
        while opcaoPerg not in [1, 2]:
            try:
                opcaoPerg = int(input("Deseja adicionar mais alguma pergunta? 1 - Sim | 2 - Não\n"))
                
                if opcaoPerg not in [1, 2]:
                    print("Tente novamente com uma opção válida! (Ex: 1 ou 2)")
            except ValueError:
                print("Por favor, digite um número inteiro (1 ou 2).")
                
        if opcaoPerg == 2:
            cont = 0
            print("Cadastro de perguntas finalizado!")

addQuestoes()

print("\n--- Resultado ---")
print("Perguntas:", perguntaAserAdd)
print("Respostas:", respostasDaQuestao)