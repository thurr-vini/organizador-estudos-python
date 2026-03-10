import os

# --- BLOCO DE FUNÇÕES ---
def exibir_menu():
    """Mostra as opções e retorna a escolha da opção"""
    # Cabeçalho
    print("\n" +"="*30)
    print("--- ORGANIZADOR DE ESTUDOS ---")
    print("="*30)

    # Menu
    print("1. Registrar Novo Estudo")
    print("2. Ver histórico de Estudos")
    print("3. Limpar Histórico de Estudos")
    print("0. Sair do Programa")
    escolha = input("\nEscolha uma opção: ")
    return escolha

def salvar_estudo(materia, minutos):
    """Calcula as horas, salva no arquivo e dá o feedback."""
    try:
        print("\nCategorias: [1] Teoria | [2] Prática | [3] Revisão")
        categorias_opcoes = input("Escolha uma categoria: ")

        categorias = {"1": "Teoria", "2": "Prática", "3": "Revisão"}

        # Se o usuário digitar algo fora de 1, 2 ou 3, vira "Outros"
        categoria = categorias.get(categorias_opcoes, "Outros") 

        minutos_int = int(minutos)
        horas = minutos_int / 60

        with open("histórico_estudos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Categoria: {categoria: <8}| Matéria: {materia} | Tempo: {minutos_int} min | Horas: {horas:.2f}h\n")

        print("\n[OK] Salvo com sucesso!")

    except ValueError:
        print("\n[ERRO] Por favor, digite apenas números para o tempo!")

def dar_incentivo(minutos):
        """Recebe o tempo e dá um incentivo baseado no tempo gasto."""
        minutos_int = int(minutos)
        horas = minutos_int / 60
        if horas < 1:
            print("Dica: Bom começo! Amanhã tente focar um pouquinho mais. Constância é tudo!")

        elif 1 <= horas < 3:
            print("Dica: Boa! Esse é o ritmo certo para quem quer aquela vaga de estágio!")

        elif horas > 3:
            print("Dica: Excelente! Você estudou acima do nível comum, parabéns!")

def mostrar_historico():
    """Exibe o histórico completo dos estudos registrados, se existir."""
    print("\n--- SEU HISTÓRICO DE ESTUDOS ---")
    if os.path.exists("histórico_estudos.txt"):
        with open("histórico_estudos.txt", "r", encoding="utf-8") as arquivo:
            print(arquivo.read())

    else:
        print("Você ainda não registrou nenhum estudo.")
    
def limpar_historico():
    """Remove o arquivo de histórico se ele existir."""
    if os.path.exists("histórico_estudos.txt"):
        confirmar = input("Tem certeza que deseja apagar TODOS os registros? (S/N):\n")
        
        if confirmar.lower() == "s":
            os.remove("histórico_estudos.txt")
            print("\n[SUCESSO] Histórico deletado!")
        else:
            print("\n[CANCELADO] O Histórico foi mantido.]")

    else:
        print("\n[ERRO] Não existe nenhum histórico para apagar.")


# --- PROGRAMA PRINCIPAL ---

while True:
    opcao = exibir_menu() # Exibe o cabeçalho com o menu e retorna o valor da opção escolhida

    # Opção 1: Registrar Novo Estudo
    if opcao == "1":
        # Coletor de dados
        materia_input = input("Que matéria você estudou hoje?\n")
        tempo_input = int(input("Quanto tempo você estudou(em minutos)?\n"))

        # Registrando novo estudo
        salvar_estudo(materia_input, tempo_input)

        # Exibir dica de incentivo
        dar_incentivo(tempo_input)
            

    # Opção 2: Ver histórico de Estudos
    elif opcao == "2":
        mostrar_historico()

    elif opcao == "0":
        print("Saindo do programa...")
        break

    elif opcao == "3":
        limpar_historico()

    else:
        print("Opção Inválida, tente novamente")

