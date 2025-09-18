tarefas = ["Estudar Python", "Fazer compras", "Ligar para o banco"]

# Usando um loop 'while' para interagir com o usuário
while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Exibir tarefas")
    print("2. Adicionar nova tarefa")
    print("3. Concluir tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    # Usando 'if/elif/else' para controlar o fluxo
    if opcao == "1":
        print("\nLista de Tarefas:")
        # Usando 'for' para exibir cada item da lista
        for tarefa in tarefas:
            print(f"- {tarefa}")

    elif opcao == "2":
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(nova_tarefa)  # Adiciona a tarefa à lista
        print(f"Tarefa '{nova_tarefa}' adicionada!")

    elif opcao == "3":
        # Combina 'for' e 'if' para mostrar as tarefas com seus índices
        print("\nQual tarefa deseja concluir?")
        for i in range(len(tarefas)):
            print(f"{i+1}. {tarefas[i]}")

        try:
            indice = int(input("Digite o número da tarefa: ")) - 1
            # 'if' para validar o input do usuário
            if 0 <= indice < len(tarefas):
                tarefa_concluida = tarefas.pop(indice)  # Remove a tarefa da lista
                print(f"Tarefa '{tarefa_concluida}' concluída e removida!")
            else:
                print("Número de tarefa inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    elif opcao == "4":
        print("Saindo do gerenciador de tarefas. Até logo!")
        break  # Sai do loop 'while'
    else:
        print("Opção inválida. Por favor, escolha uma das opções acima.")